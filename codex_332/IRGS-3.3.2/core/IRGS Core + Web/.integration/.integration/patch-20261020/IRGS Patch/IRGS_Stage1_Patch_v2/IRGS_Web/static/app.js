'use strict';
const $=selector=>document.querySelector(selector);
const esc=value=>String(value??'').replace(/[&<>"']/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
const label=value=>String(value??'').replaceAll('_',' ').replace(/\b\w/g,char=>char.toUpperCase());
const rows=value=>Array.isArray(value)?value.map((item,index)=>item&&typeof item==='object'?item:{id:String(index),name:String(item)}):Object.entries(value||{}).map(([id,item])=>item&&typeof item==='object'?{id,...item}:{id,name:String(item)});
let token,current=null,currentBinding=null,view='story',workspaceMode='player',busy=false,library={},deleteTarget=null,campaignRequest=0,loadingCampaign=false;
let historicalCatalogue=null,historicalEntryId=null,historicalPreview=null,historicalRequest=0,historicalLoading=false;
let wizardStep=0,startingOptions=null,startingRequest=0,startingLoading=false,reviewSelection=null,chronicleRequest=0,chronicleCursor=null,transportPending=null,inspectorRequest=0;
const scrollPositions=new Map();
const defaultPreferences={theme:'parchment',font:'serif',fontSize:18,lineHeight:1.8,width:740,mechanics:'concise',motion:'system',submitKey:'ctrl-enter'};
function readLocal(key,fallback=null){try{const value=localStorage.getItem(key);return value===null?fallback:JSON.parse(value);}catch{return fallback;}}
function writeLocal(key,value){try{if(value===null)localStorage.removeItem(key);else localStorage.setItem(key,JSON.stringify(value));}catch{}}
let preferences={...defaultPreferences,...readLocal('irgs-reading-preferences',{})};
function notice(text,error=false){$('#notice').textContent=text;$('#notice').className=error?'error':'';}
async function api(path,body,options={}){
  const creator=options.creator??workspaceMode==='creator';
  if(creator&&!/[?&]mode=/.test(path))path+=(path.includes('?')?'&':'?')+'mode=creator';
  const headers={'X-IRGS-Token':token||''};
  const request={headers};
  if(body!==undefined){headers['Content-Type']='application/json';request.method='POST';request.body=JSON.stringify(creator?{...body,mode:'creator'}:body);}
  const response=await fetch('/api/'+path,request);
  let result;try{result=await response.json();}catch{const error=new Error('The host returned an unreadable response. Check the saved request before retrying.');error.status=response.status;throw error;}
  if(!response.ok){const error=new Error(result.error||'Request failed');error.status=response.status;error.data=result;throw error;}
  return result;
}
function profileId(){return current?.binding?.campaign_profile||current?.state?.binding?.campaign_profile||'ast';}
function profileInfo(){return rows(library.campaign_profiles).find(profile=>profile.id===profileId())||{};}
function actors(){return workspaceMode==='creator'?current?.state?.actors||{}:Object.fromEntries([...(current?.known_actors||[]),...(current?.character?[current.character]:[])].map(actor=>[actor.id,actor]));}
function playerActor(){return current?.actor_id||null;}
function registry(id){return workspaceMode==='creator'?current?.state?.registry?.characters?.[id]||{}:{};}
function valueText(value){if(value===null||value===undefined)return 'Not established';if(typeof value==='object')return 'value'in value?String(value.value):JSON.stringify(value);return String(value);}
function facts(object,empty='No accessible records are established.'){return Object.entries(object||{}).map(([key,value])=>`<div class="list-row"><small>${esc(label(key))}</small><strong>${esc(valueText(value))}</strong></div>`).join('')||`<p class="note">${esc(empty)}</p>`;}
function records(items,empty){const list=rows(items);return list.length?list.map(item=>`<article class="record-card"><h3>${esc(item.name||item.title||item.description||item.id||'Record')}</h3>${facts(Object.fromEntries(Object.entries(item).filter(([key])=>!['name','title','id'].includes(key))))}</article>`).join(''):`<p class="note">${esc(empty)}</p>`;}
function viewKey(name=view){return [current?.id||'',current?.actor_id||'',workspaceMode,name].join(':');}
function rememberScroll(){if(current)scrollPositions.set(viewKey(),$('#content').scrollTop||0);}
function restoreScroll(){const key=viewKey();requestAnimationFrame(()=>{if(key===viewKey())$('#content').scrollTop=scrollPositions.get(key)||0;});}
function draftKey(){return current?`irgs-draft:${current.id}:${current.actor_id||'none'}`:null;}
function pendingKey(){return current?`irgs-pending:${current.id}:${current.actor_id||'none'}`:null;}
function stashDraft(){const key=draftKey();if(key)writeLocal(key,$('#declaration').value||'');}
function loadDraft(){const key=draftKey();$('#declaration').value=key?readLocal(key,''):'';transportPending=pendingKey()?readLocal(pendingKey()):null;}
function displayTime(){const time=current?.campaign_time||{};return [time.date||time.calendar_date||(time.day!==undefined?'Day '+time.day:null),time.time||'time unknown',time.precision&&time.precision!=='exact'?time.precision:null].filter(Boolean).join(' · ');}
async function refreshList(selected){const data=await api('campaigns');token=data.token;$('#campaign').innerHTML='<option value="">Choose a campaign</option>'+data.campaigns.map(campaign=>`<option value="${esc(campaign.id)}">${esc(campaign.name)}</option>`).join('');if(selected)$('#campaign').value=selected;return data.campaigns;}
function syncControls(){
  const selected=current&&!loadingCampaign&&$('#campaign').value===current.id;
  $('#campaign').disabled=busy||!token;$('#player-character').disabled=busy||!selected||!(current?.controlled_actors||[]).length;
  $('#new-campaign').disabled=busy||!token;$('#workspace-mode').disabled=busy||!token;
  $('#export').disabled=$('#delete-campaign').disabled=busy||!selected;$('#fork').disabled=busy||!selected||workspaceMode!=='creator';
  $('#fork').hidden=workspaceMode!=='creator';$('#creator-nav').hidden=workspaceMode!=='creator';$('#library-nav').hidden=workspaceMode!=='creator';
  $('#workspace-mode').textContent=workspaceMode==='creator'?'Return to player view':'Creator workspace';$('#mode-label').textContent=workspaceMode==='creator'?'Creator access · full records':'Player view · filtered by the server';
  $('#mode-badge').textContent=workspaceMode==='creator'?'CREATOR WORKSPACE':'PLAYER VIEW';$('#export').textContent=workspaceMode==='creator'?'Export full save':'Export known view';
  $('#saved').textContent=busy?'Saving…':loadingCampaign?'Loading campaign…':current?`Saved · revision ${current.revision}`:'Local host connected';
  syncCreateControls();syncComposer();
}
function setBusy(value){busy=value;syncControls();}
async function openCampaign(id,options={}){
  stashDraft();rememberScroll();const request=++campaignRequest,selected=id||'',mode=workspaceMode;
  $('#campaign').value=selected;current=null;currentBinding=null;transportPending=null;loadingCampaign=Boolean(selected);render();
  if(!selected){localStorage.removeItem('irgs-active');return true;}
  const query=new URLSearchParams();if(options.actorId)query.set('actor_id',options.actorId);
  try{const result=await api('playthrough/'+encodeURIComponent(selected)+(query.size?'?'+query.toString():''),undefined,{creator:mode==='creator'});
    if(request!==campaignRequest||$('#campaign').value!==selected||workspaceMode!==mode)return false;
    if(result.id!==selected||(mode==='player'&&Object.prototype.hasOwnProperty.call(result,'state')))throw new Error('The host returned an incompatible playthrough view.');
    current=result;currentBinding=result.binding;loadingCampaign=false;localStorage.setItem('irgs-active',selected);
    $('#player-character').innerHTML=(result.controlled_actors||[]).map(actor=>`<option value="${esc(actor.id)}">${esc(actor.name)}</option>`).join('')||'<option value="">No selected player character</option>';$('#player-character').value=result.actor_id||'';
    loadDraft();render();restoreScroll();return true;
  }catch(error){if(request!==campaignRequest||$('#campaign').value!==selected||workspaceMode!==mode)return false;loadingCampaign=false;render();throw error;}
}
function changeView(next){rememberScroll();stashDraft();view=next;document.body.classList.remove('nav-open');$('#toggle-nav').setAttribute('aria-expanded','false');render();restoreScroll();}
function empty(){return '<div class="empty"><div class="eyebrow">WELCOME TO IRGS</div><h2>A world worth returning to.</h2><p>Create a campaign, choose a starting point, and make it your own.</p><button id="empty-create" class="primary">Create a campaign →</button></div>';}
function render(){
  const headings={story:['Story','Your next meaningful choice.'],world:['World','Inspect what your character can access.'],chronicle:['Chronicle','The record available to your character.'],creator:['Creator workspace','Explicitly sourced changes to the authoritative world.'],library:['Engines & libraries','Creator reference material.'],trash:['Campaign Trash','Recover complete saved campaigns.'],'content-library':['Content Library','Choose a campaign and an entry point.']};
  const heading=headings[view]||(view.startsWith('feature:')?[(features.find(f=>f.id===view.slice(8))||{}).label||'Feature','Planned feature. Nothing here is live.']:headings.story);$('#section-label').textContent=heading[0].toUpperCase();$('#page-title').textContent=current?current.name:'A world worth returning to.';$('#page-subtitle').textContent=heading[1];
  $('#header-campaign').textContent=current?.name||'Your campaign';$('#world-time').textContent=current?displayTime():'No campaign selected';$('#header-scene').textContent=current?.scene?.location||current?.scene?.title||'Persistent local worlds';
  $('#binding-badge').textContent=current?'Core '+(current.binding?.core||'3.3')+' · '+label(current.binding?.genre_id||'campaign'):'CORE 3.3';
  document.querySelectorAll('[data-view]').forEach(button=>{const active=button.dataset.view===view;button.classList.toggle('selected',active);if(button.getAttribute('role')==='tab'){button.setAttribute('aria-selected',String(active));button.tabIndex=active?0:-1;}});
  $('#content').setAttribute('aria-label',heading[0]);$('#content').setAttribute('aria-labelledby',['story','world','chronicle'].includes(view)?'tab-'+view:'page-title');syncControls();renderContext();
  if(loadingCampaign){$('#content').innerHTML='<div class="empty">Loading the selected campaign…</div>';return;}
  if(view==='trash'){renderTrash();return;}if(view==='library'){renderLibrary();return;}if(view==='content-library'){renderContentLibrary();return;}if(view.startsWith('feature:')){renderFeature(view.slice(8));return;}
  if(!current){$('#content').innerHTML=empty();$('#empty-create').onclick=openCreateDialog;return;}
  ({story:renderStory,world:renderWorld,chronicle:renderChronicle,creator:renderCreator}[view]||renderStory)();
}
function entryMarkup(entry){
  const status=entry.status||'',kind=entry.kind||'record',title=entry.title||label(kind),text=entry.text??entry.declaration??entry.assertion??'';
  const times=[['occurred',entry.occurrence_at],['observed',entry.observed_at],['transmitted',entry.transmitted_at],['recorded',entry.recorded_at],['received',entry.received_at]].filter(([,value])=>value!==undefined&&value!==null).map(([name,value])=>name+' '+valueText(value));
  const gap=entry.source_available===false||entry.source_gap;
  return `<article class="feed-entry ${esc(kind)}" id="entry-${esc(entry.id)}"><div class="entry-meta"><span>${esc(title)}</span>${status?`<span class="badge">${esc(label(status))}</span>`:''}</div><div class="entry-text">${esc(text)}</div>${times.length?`<p class="note">${esc(times.join(' · '))}</p>`:''}${gap?`<p class="source-gap note">${esc(entry.gap_note||'The original source text is unavailable; no transcript has been reconstructed.')}</p>`:''}${entry.source_refs?.length?`<details class="mechanical-detail" ${preferences.mechanics==='expanded'?'open':''}><summary>Source and record details</summary><p>${esc(entry.source_refs.join(' · '))}</p></details>`:''}<button type="button" class="bookmark quiet" data-bookmark="${esc(entry.id)}" aria-pressed="false">Bookmark</button></article>`;
}
function renderStory(){
  const scene=current.scene||{},entries=rows(current.story||current.chronicle),key='irgs-bookmarks:'+current.id,bookmarks=new Set(readLocal(key,[]));
  $('#content').innerHTML=`<div class="story-reading"><header class="scene-header"><span class="eyebrow">${esc(scene.location||'CURRENT SCENE')}</span><h2>${esc(scene.title||'Your saved checkpoint')}</h2>${scene.description?`<p>${esc(valueText(scene.description))}</p>`:''}</header><div class="story-tools"><label class="sr-only" for="story-search">Search available scene records</label><input id="story-search" type="search" placeholder="Search available records…"><button id="jump-latest" class="quiet" type="button">Latest ↓</button></div>${!current.capabilities?.narrator?'<p class="capability-note">The host preserves declarations and received records. A general narrator is not connected; an attempt remains pending until it is resolved or withdrawn.</p>':''}<div id="story-feed"></div><div id="feed-end" tabindex="-1"></div></div>`;
  $('#declaration').placeholder=current.opening?.status==='awaiting_first_action'?'Your first move: say or do anything. It is saved exactly as written.':'Describe what your character says or attempts…';
  const draw=()=>{const query=$('#story-search').value.toLowerCase();const filtered=entries.filter(entry=>`${entry.text||''} ${entry.title||''}`.toLowerCase().includes(query));$('#story-feed').innerHTML=filtered.map(entryMarkup).join('')||'<div class="story-empty"><h3>The next choice is yours.</h3><p>No matching narrative or action records are available. Your confirmed checkpoint remains intact.</p></div>';document.querySelectorAll('[data-bookmark]').forEach(button=>{button.setAttribute('aria-pressed',String(bookmarks.has(button.dataset.bookmark)));button.textContent=bookmarks.has(button.dataset.bookmark)?'Bookmarked':'Bookmark';button.onclick=()=>{bookmarks.has(button.dataset.bookmark)?bookmarks.delete(button.dataset.bookmark):bookmarks.add(button.dataset.bookmark);writeLocal(key,[...bookmarks]);button.setAttribute('aria-pressed',String(bookmarks.has(button.dataset.bookmark)));button.textContent=bookmarks.has(button.dataset.bookmark)?'Bookmarked':'Bookmark';};});};
  $('#story-search').oninput=draw;draw();$('#jump-latest').onclick=()=>$('#feed-end').scrollIntoView({behavior:preferences.motion==='reduce'?'instant':'auto',block:'end'});
}
function renderWorld(){
  const world=current.world||{};
  $('#content').innerHTML=`<div class="world-workspace"><div class="panel"><span class="eyebrow">ONE AUTHORITATIVE WORLD</span><h2>The world you can inspect.</h2><p>These records reflect the selected character’s access. Looking around this workspace does not issue an order or advance the clock.</p></div><div class="world-grid"><section class="panel"><h3>Inventory & resources</h3>${records(world.inventory||current.inventory,'No accessible physical inventory records have been established. Quantities remain unknown.')}<button class="quiet" data-inspect="inventory">Inspect inventory</button></section><section class="panel"><h3>People & institutions</h3>${records(world.institutions||world.factions,'No accessible institution or faction records are available.')}<button class="quiet" data-inspect="factions">Inspect institutions</button></section><section class="panel"><h3>Projects & commitments</h3>${records(world.activities,'No accessible project progress is established.')}<button class="quiet" data-inspect="projects">Inspect projects</button></section><section class="panel"><h3>Known places</h3>${records(world.locations,'No known atlas or route records are supplied.')}<button class="quiet" data-inspect="map">Inspect known places</button></section></div><section class="panel time-controls"><h3>Time advancement</h3><p>Elapsed-time advancement is unavailable because this campaign has no configured elapsed-time binding and automatic resolver.</p><label>Requested duration<select id="advance-duration" disabled><option>Until the next required decision</option><option>One hour</option><option>One day</option><option>One week</option><option>One month</option><option>One year</option></select></label><button class="primary" disabled>Time advancement unavailable</button><small>Scene dates and causal record order are preserved. No duration is inferred from the event counter.</small></section></div>`;
  bindInspectors();
}
async function renderChronicle(){
  const request=++chronicleRequest,campaign=current.id,actor=current.actor_id,mode=workspaceMode;
  let searchRequest=0;
  $('#content').innerHTML='<div class="chronicle-workspace"><div class="panel"><h2>Your available history.</h2><form id="chronicle-search"><label>Archive area<select name="area"><option value="timeline">Historical timeline</option><option value="personal">Personal chronicle</option><option value="biographies">Biographies</option><option value="relationships">Relationships</option><option value="institutions">Institutional history</option><option value="archive">Historical archive</option></select></label><label>Search accessible records<input name="q" type="search" placeholder="Event, person or source phrase"></label><button class="primary">Search Chronicle</button></form><p class="note">Only records returned for this character’s scope are shown. Original text and receipt dates retain their meaning.</p></div><div id="chronicle-results" aria-live="polite"></div></div>';
  const load=async(cursor=null)=>{const search=++searchRequest;const fields=Object.fromEntries(new FormData($('#chronicle-search'))),query=new URLSearchParams({...fields,limit:'30'});if(actor)query.set('actor_id',actor);if(cursor)query.set('cursor',cursor);$('#chronicle-results').innerHTML='<p class="note">Loading accessible history…</p>';try{const result=await api('chronicle/'+campaign+'?'+query.toString());if(search!==searchRequest||request!==chronicleRequest||view!=='chronicle'||current?.id!==campaign||current.actor_id!==actor||workspaceMode!==mode)return;const memory=result.memory||{};$('#chronicle-results').innerHTML=`<section class="panel archive-status"><h3>Historical memory</h3><p>${esc(memory.reason||'Archive periods require committed calendar boundaries.')}</p><small>Status: ${esc(memory.status||'unconfigured')} · summary budgets: ${esc(memory.budget_policy?.status||'unconfigured')}</small><p class="note">The consolidation structure is annual → five-year → twenty-five-year → expanding century records → sealed 500-year epochs. No summary is generated by inspecting this screen.</p></section><section class="panel">${(result.entries||[]).map(entryMarkup).join('')||'<p class="note">No accessible records match this area and search.</p>'}${result.pagination?.next_cursor?'<button id="chronicle-next" class="quiet">Next records →</button>':''}</section>`;if($('#chronicle-next'))$('#chronicle-next').onclick=()=>load(result.pagination.next_cursor);}catch(error){if(search===searchRequest&&request===chronicleRequest&&view==='chronicle')$('#chronicle-results').innerHTML=`<p class="note">${esc(error.message)}</p>`;}};
  $('#chronicle-search').onsubmit=event=>{event.preventDefault();load();};load();
}
function renderContext(){
  if(!current){$('#context-content').innerHTML='<p class="note">Select a campaign to inspect its available context.</p>';return;}
  const character=current.character,known=rows(current.known_actors).filter(actor=>actor.id!==character?.id),orders=rows(current.orders),obligations=rows(current.world?.obligations);
  $('#context-content').innerHTML=`<section><span class="eyebrow">YOUR CHARACTER</span><h2>${esc(character?.name||'No selected player character')}</h2>${character?facts(character.current):'<p class="note">This saved campaign has no selected player character. Choose or create one in the explicit Creator workspace.</p>'}<button class="quiet" data-inspect="character">Character details</button></section><section><h3>Known people</h3>${known.slice(0,6).map(actor=>`<p>${esc(actor.name)}${actor.role?`<small>${esc(actor.role)}</small>`:''}</p>`).join('')||'<p class="note">No other identities have been received.</p>'}</section><section><h3>Received orders</h3>${orders.map(order=>`<p>${esc(order.content||order.text||order.description||'Order record')}<small>${order.executed?'Recorded as executed':'Receipt does not establish execution'}</small></p>`).join('')||'<p class="note">No received orders are available.</p>'}</section><section><h3>Known commitments</h3>${obligations.map(item=>`<p>${esc(item.description||item.title||item.id)}<small>${esc(item.status||'status unknown')}</small></p>`).join('')||'<p class="note">No accessible obligations are recorded.</p>'}</section>`;
  bindInspectors();
}
function bindInspectors(){document.querySelectorAll('[data-inspect]').forEach(button=>button.onclick=()=>openInspector(button.dataset.inspect));}
async function openInspector(kind){
  if(!current)return;const inspect=++inspectorRequest;const world=current.world||{},titles={character:'Character',inventory:'Inventory',relationships:'Relationships',map:'Known places',projects:'Projects & research',factions:'Institutions & factions'};$('#inspect-title').textContent=titles[kind]||'Campaign information';
  const character=current.character;
  if(kind==='character')$('#inspect-content').innerHTML=character?`<h3>${esc(character.name)}</h3><p>${esc(character.species||'Species not established')}</p>${facts(character.current)}<p class="note">Capability ratings, affiliations and possessions appear only when provided as accessible records.</p>`:'<p>No selected player character is available.</p>';
  if(kind==='inventory')$('#inspect-content').innerHTML=records(current.inventory||world.inventory,'No accessible inventory instances are supplied. Ownership, custody, carried location, storage, accessibility and condition remain distinct; none have been inferred from a description.');
  if(kind==='relationships')$('#inspect-content').innerHTML=records(current.relationships||world.relationships,'No accessible relationship or family-tree records have been established.');
  if(kind==='map')$('#inspect-content').innerHTML=records(world.locations,'No known map, routes or atlas are available. Inspecting a location would not move the character.');
  if(kind==='projects')$('#inspect-content').innerHTML=records(world.activities||world.projects,'No accessible projects, research progress or completed outputs are established.');
  if(kind==='factions')$('#inspect-content').innerHTML=records(world.institutions||world.factions,'No accessible institution or faction-control records are established. Existence, participation and control require separate evidence.');
  if(!$('#inspect-dialog').open)$('#inspect-dialog').showModal();
  if(kind==='factions'){const id=current.id,request=campaignRequest;try{const result=await api('availability/'+id+(current.actor_id?'?actor_id='+encodeURIComponent(current.actor_id):''));if(inspect===inspectorRequest&&request===campaignRequest&&current?.id===id&&$('#inspect-dialog').open)$('#inspect-content').innerHTML=records(result.entities?.factions||result.factions,result.reason||'No accessible current factions are established.');}catch(error){notice(error.message,true);}}
}
function renderCreator(){
  if(workspaceMode!=='creator'||!current?.state){$('#content').innerHTML='<div class="empty">Choose Creator workspace explicitly to inspect full records or apply sourced host decisions.</div>';return;}
  renderCreatorJournal();$('#content').insertAdjacentHTML('afterbegin','<section class="panel creator-warning"><span class="eyebrow">FULL RECORD ACCESS</span><h2>Creator tools</h2><p>These controls can inspect and change authoritative records. Player views remain server-filtered when you return.</p><div id="host-tools"></div></section>');mountTools();if(current.state.historical_start)$('#content').insertAdjacentHTML('afterbegin',historicalReferenceMarkup(current.state.historical_start));
}
async function mutate(path,payload){
  if(workspaceMode!=='creator'||busy||loadingCampaign||!current?.state||$('#campaign').value!==current.id)return;
  const target={id:current.id,revision:current.revision},request=campaignRequest;setBusy(true);
  try{const result=await api(path,{...target,...payload});if(request!==campaignRequest||current?.id!==target.id)return;await openCampaign(target.id,{actorId:current.actor_id});notice(result.last_result?.deferred?.length?'Request intent was preserved as unresolved.':'Host decision saved to the authoritative campaign.');}catch(error){notice(error.message,true);}finally{setBusy(false);}
}
function submit(op,params){return mutate('event',{op,params});}function submitBatch(events){return mutate('frontier',{events});}
function textItems(value) {return (Array.isArray(value)?value:value?[value]:[]).map(item=>typeof item==='string'?item:item.statement || item.text || item.summary || JSON.stringify(item));}
function safeHttpUrl(value) {try{const url=new URL(value);return ['http:','https:'].includes(url.protocol)?url.href:null;}catch{return null;}}
function historicalSnapshotMarkup(snapshot) {
  const opening=snapshot.opening || {},briefing=textItems(snapshot.briefing),domains=snapshot.domains || {},sources=snapshot.sources || [];
  return `<div class="historical-opening"><div class="eyebrow">DATED OPENING REFERENCE</div><h3>${esc(opening.label || opening.date || 'Opening date not specified')}</h3><p class="note">${esc(label(opening.calendar || 'calendar unspecified'))} calendar · ${opening.time?esc(opening.time):'hour unknown'}${opening.precision?' · '+esc(opening.precision)+' precision':''}</p>${opening.boundary?`<p>${esc(opening.boundary)}</p>`:''}<p class="reference-note">Historical setup material for the campaign creator. It does not automatically establish what a player character knows.</p>${briefing.map(text=>`<p>${esc(text)}</p>`).join('')}${entryGuideMarkup(snapshot.entry_guide)}<div class="historical-domains">${['political','military','territorial','diplomatic'].map(key=>`<section><h3>${label(key)}</h3>${(domains[key] || []).map(item=>`<p>${esc(typeof item==='string'?item:item.statement)}${item.source_ids?.length?` <small>[${esc(item.source_ids.join(', '))}]</small>`:''}</p>`).join('') || '<p class="note">No opening record supplied.</p>'}</section>`).join('')}</div>${snapshot.actors?.length?`<details><summary>Named historical actors</summary>${snapshot.actors.map(actor=>`<div class="list-row"><strong>${esc(actor.name)}</strong><small>${esc(actor.role || '')}</small></div>`).join('')}</details>`:''}<h3 class="spacer">Unknowns and setup limits</h3>${textItems(snapshot.unknowns).map(text=>`<p class="note">${esc(text)}</p>`).join('') || '<p class="note">No additional unknowns are listed in this reference.</p>'}${snapshot.simulation_rules?.length?`<details><summary>Campaign use</summary>${textItems(snapshot.simulation_rules).map(text=>`<p>${esc(text)}</p>`).join('')}</details>`:''}<details><summary>Historical sources</summary>${sources.map(source=>{const url=safeHttpUrl(source.url),title=source.title || source.id || 'Source';return `<p>${source.id?`<small>${esc(source.id)} · </small>`:''}${url?`<a href="${esc(url)}" target="_blank" rel="noopener noreferrer">${esc(title)}</a>`:esc(title)}</p>`;}).join('') || '<p class="note">No source links supplied.</p>'}</details><p class="note">Later outcomes come from campaign events. This opening reference does not schedule future historical results.</p></div>`;
}
function historicalReferenceMarkup(start) {
  const snapshot=start?.snapshot;
  if(!snapshot)return '';
  return `<details class="panel historical-reference"><summary>Opening reference · ${esc(snapshot.opening?.label || start.date || 'Historical start')}</summary><p class="reference-note">Preserved opening context. Later campaign events determine the current world state.</p>${historicalSnapshotMarkup(snapshot)}<p class="note">Historical archive policy: ${esc(start.history_origin?.status==='unbound'?'unconfigured':start.history_origin?.status || 'unconfigured')}. Opening provenance is retained for later calendar and history integration.</p></details>`;
}

const operations = {
 register_actor:['Register a character',{actor_id:'text',name:'text',species:'text',player_controlled:['false','true'],instruction_ref:'text'}],
 set_scene:['Set the scene',{day:'number',time:'text',precision:['approximate','exact','unknown'],description:'textarea',instruction_ref:'text'}],
 record_evidence:['Record evidence',{evidence_id:'text',subject:'actor',assertion:'textarea',status:['established','testimony','inference','provisional','unknown','superseded']}],
 receive_evidence:['Receive evidence',{evidence_id:'text',recipient:'actor'}],
 confirm_character_field:['Confirm character state',{subject:'actor',evidence_id:'text',field:['location','condition','custody','service','current_activity'],value:'text',authority_ref:'text',instruction_ref:'text'}],
 establish_stock:['Establish inventory',{location:'text',material:'text',quantity:'number',inventory_evidence_ref:'text'}],
 transfer_stock:['Transfer inventory',{from:'text',to:'text',material:'text',quantity:'number',authority_ref:'text'}],
 record_obligation:['Record an obligation',{obligation_id:'text',subject:'actor',description:'textarea',status:['offered','agreed','due','disputed','fulfilled','unknown'],instruction_ref:'text'}],
 record_design:['Record a design',{design_id:'text',name:'text'}],
 receive_order:['Receive an order',{order_id:'text',recipient:'actor',content:'textarea',authority_ref:'text'}],
 record_capacity:['Record site capacity',{capacity_id:'text',site:'text',quantity:'number',unit:['concurrent_people']}],
 commit_activity:['Commit a sourced activity',{activity_id:'text',actors:'actors',site:'text',capacity_id:'text',start:'number',end:'number',role:'text',authority_ref:'text',instruction_ref:'text'}],
 record_delegation:['Record delegated authority',{delegation_id:'text',principal:'actor',delegate:'actor',actors:'actors',site:'text',start:'number',end:'number',role:'text',authority_ref:'text',instruction_ref:'text'}]
};
function mountTools() {
  $('#host-tools').innerHTML = `<h2>Record a world event</h2><p class="note">Every event runs through dependency observation. Single invalid events are rejected. Simultaneous requests retain unresolved intent when they conflict or fail their current preconditions.</p><label>Operation<select id="operation">${Object.entries(operations).map(([id,[name]])=>`<option value="${id}">${name}</option>`).join('')}</select></label><form id="event-form"><div id="fields"></div><label>Source reference<input name="source_ref" required placeholder="Source establishing this event"></label><div class="buttons"><button class="primary">Submit event</button></div></form><details><summary>Submit simultaneous requests as JSON</summary><p class="note">Enter 1–16 objects with op and params. All requests use the same next causal sequence and this campaign’s scope. Shared resources can defer conflicting requests.</p><form id="batch-form"><label>Requests<textarea name="events" required maxlength="80000" aria-label="Simultaneous requests JSON" placeholder='[{"op":"record_design","params":{"design_id":"draft","name":"Draft","source_ref":"session reference"}}]'></textarea></label><div class="buttons"><button class="primary">Submit simultaneous requests</button></div></form></details>`;
  function fields() { $('#fields').innerHTML = Object.entries(operations[$('#operation').value][1]).map(([key,type])=>{
    let control;
    if (type === 'actor' && Object.keys(actors()).length) control = `<select name="${key}">${Object.entries(actors()).map(([id,a])=>`<option value="${esc(id)}">${esc(a.name || id)} · ${esc(id)}</option>`).join('')}</select>`;
    else if (Array.isArray(type)) control = `<select name="${key}">${type.map(v=>`<option value="${v}">${label(v)}</option>`).join('')}</select>`;
    else if (type === 'textarea') control = `<textarea name="${key}" required maxlength="10000"></textarea>`;
    else control = `<input name="${key}" type="${type==='actor'||type==='actors'?'text':type}" required ${type === 'number' ? 'min="0" step="1"' : 'maxlength="2000"'} ${type==='actors'?'placeholder="Actor IDs, comma separated"':''} ${key==='day' ? `value="${current.state.campaign_time?.day || 1}"` : ''}>`;
    return `<label>${label(key)}${control}</label>`;
  }).join(''); }
  fields(); $('#operation').onchange = fields;
  $('#event-form').onsubmit=e=>{e.preventDefault();const op=$('#operation').value,params=Object.fromEntries(new FormData(e.target));for(const [k,t] of Object.entries(operations[op][1])) {if(t==='number')params[k]=Number(params[k]);if(t==='actors')params[k]=params[k].split(',').map(id=>id.trim()).filter(Boolean);}if(op==='register_actor')params.player_controlled=params.player_controlled==='true';submit(op,params);};
  $('#batch-form').onsubmit=e=>{e.preventDefault();try{submitBatch(JSON.parse(new FormData(e.target).get('events')));}catch(err){notice('Invalid requests JSON: '+err.message,true);}};
}

function renderCreatorJournal() {
  const events=[...(current.state.journal || [])].reverse(), pending=Object.entries(current.state.r9?.requests || {}).filter(([,r])=>r.status==='unresolved'), mandates=Object.entries(current.state.r9?.mandates || {});
  $('#content').innerHTML=`<article class="panel"><div class="eyebrow">DURABLE REQUESTS</div><h2>${pending.length} unresolved request${pending.length===1?'':'s'}</h2>${pending.map(([id,r])=>`<details open><summary>${esc(label(r.original.op))} · ${esc(id)}</summary><p>${esc(r.reason || 'Dependency conflict')}</p><pre>${esc(JSON.stringify(r.original,null,2))}</pre></details>`).join('') || '<p>No unresolved requests.</p>'}<h2 class="spacer">Decision authority</h2><p class="note">Record an actual scoped mandate before deciding. Approval rechecks current state and executes later; denial preserves the request without applying it.</p><form id="mandate-form"><label>Mandate ID<input name="mandate_id" required maxlength="200"></label><label>Authorized actor<input name="actor" required maxlength="200"></label><label>Operation rights, comma separated<input name="operations" required placeholder="transfer_stock"></label><label>Authority source reference<input name="source_ref" required maxlength="2000"></label><div class="buttons"><button class="primary">Record mandate</button></div></form>${pending.length?`<h2 class="spacer">Resolve a request</h2><form id="resolve-form"><label>Request<select name="request_id">${pending.map(([id,r])=>`<option value="${esc(id)}">${esc(r.original.op)} · ${esc(id)}</option>`).join('')}</select></label><label>Mandate<select name="mandate_id">${mandates.map(([id,m])=>`<option value="${esc(id)}">${esc(id)} · ${esc(m.actor)}</option>`).join('')}</select></label><label>Authorized actor<input name="actor" required maxlength="200"></label><label>Decision<select name="approve"><option value="true">Approve and execute if valid</option><option value="false">Deny</option></select></label><div class="buttons"><button class="primary" ${mandates.length?'':'disabled'}>Record decision</button></div></form>`:''}<h2 class="spacer">Decision history</h2>${facts(current.state.r9?.decisions)}<h2 class="spacer">${events.length} recorded event${events.length===1?'':'s'}</h2>${events.map(e=>`<details><summary>Sequence ${esc(e.at)} · ${esc(label(e.op.replace(/^ast_/,'')))}</summary><p class="note">${esc(e.id)}</p><pre>${esc(JSON.stringify(e.params,null,2))}</pre></details>`).join('')||'<p>Your first committed event will appear here.</p>'}</article>`;
  $('#mandate-form').onsubmit=e=>{e.preventDefault();const data=Object.fromEntries(new FormData(e.target));data.operations=data.operations.split(',').map(op=>op.trim()).filter(Boolean);mutate('mandate',data);};
  if ($('#resolve-form')) $('#resolve-form').onsubmit=e=>{e.preventDefault();const data=Object.fromEntries(new FormData(e.target));data.decision_id=crypto.randomUUID();data.approve=data.approve==='true';mutate('resolve',data);};
}

function catalogCards(items,kind) {
  return rows(items).map(item=>{
    const details=Object.fromEntries(['id','version','genre_id','library_ids','runtime_operations','specialty_runtime_operations','lookup_operations','profile_requirements','source_files','receiving_binding','lookup_creates_state','automatic_numeric_adoption','numeric_profile_adoption'].filter(key=>key in item).map(key=>[key,item[key]]));
    return `<article class="panel"><span class="badge">${esc(item.type==='campaign_library'?'CAMPAIGN CONTENT LIBRARY':kind)}</span><h2>${esc(item.name || item.title || item.id)}</h2><p>${esc(item.description || item.summary || item.source_status || item.scope || item.certification || '')}</p>${item.status?`<small>${esc(label(item.status.toLowerCase()))}</small>`:''}${(item.limitations || []).map(text=>`<p class="note">${esc(text)}</p>`).join('')}<details><summary>Operations and source references</summary>${facts(details)}</details></article>`;
  }).join('');
}
function renderLibrary() {
  if(workspaceMode!=='creator'){$('#content').innerHTML='<div class="empty">Source-library inspection belongs to the explicit Creator workspace or campaign setup. Reference content does not become character knowledge.</div>';return;}
  const core=library.core || {};
  $('#content').innerHTML=`<article class="panel scene"><div class="eyebrow">INTERACTIVE ROLEPLAYING GAMES SYSTEMS</div><h2>Core ${esc(core.version || '3.3')} is the foundation.</h2><p>Genre engines add domain rules. Content libraries supply references and campaign material. A campaign selects those components and stores its own facts in one world state.</p></article><article class="panel spacer"><h2>Search source content</h2><p class="note">Inspect packaged references and their original status. Looking up a record creates no campaign effects or authority.</p><form id="content-search"><label>Content library<select name="library">${rows(library.content_libraries).map(item=>`<option value="${esc(item.id)}">${esc(item.name || item.id)}</option>`).join('')}</select></label><label>Search text<input name="q" maxlength="2000" placeholder="Name, template, rule or source phrase"></label><div class="buttons"><button class="primary">Search content</button></div></form><div id="content-results"></div></article><h2 class="spacer">Core</h2><div class="cards">${catalogCards([core],'CORE')}</div><h2 class="spacer">Genre engines</h2><div class="cards">${catalogCards(library.genre_engines,'GENRE ENGINE')}</div><h2 class="spacer">Content libraries</h2><div class="cards">${catalogCards(library.content_libraries,'CONTENT LIBRARY')}</div><h2 class="spacer">Campaign profiles</h2><div class="cards">${catalogCards(library.campaign_profiles,'CAMPAIGN PROFILE')}</div>`;
  $('#content-search').onsubmit=async e=>{e.preventDefault();const button=e.target.querySelector('button');button.disabled=true;try{const query=new URLSearchParams(new FormData(e.target));query.set('limit','30');const result=await api('content?'+query.toString());$('#content-results').innerHTML=`<p class="note">Source status: ${esc(result.source_status)} · ${result.results.length} result${result.results.length===1?'':'s'}</p>${result.results.map(row=>`<details><summary>${esc(Object.values(row.identity || {}).join(' · ') || row.source_file)}${row.line?' · line '+esc(row.line):''}</summary><p class="note">${esc(row.source_file)}</p>${row.source_status_fields?facts(row.source_status_fields):''}<pre>${esc(row.excerpt)}</pre></details>`).join('') || '<p>No matching source records.</p>'}`;}catch(err){notice(err.message,true);}finally{button.disabled=false;}};
}

let features=[];
const LIFECYCLE_LABEL={planned:'Planned',scaffold:'Scaffold',in_development:'In development',functional:'Available',deferred:'Deferred'};
function featureNavMarkup(){return features.filter(f=>!f.parentId&&f.id!=='my-campaigns').map(f=>`<button data-view="${f.id==='content-library'?'content-library':'feature:'+esc(f.id)}" data-feature="${esc(f.id)}">${esc(f.label)}${f.lifecycle==='functional'?'':` <small class="badge">${esc(LIFECYCLE_LABEL[f.lifecycle]||f.lifecycle)}</small>`}</button>`).join('');}
async function loadFeatureNav(){
  features=(await api('features',undefined,{creator:false})).features||[];
  const nav=$('#feature-nav');if(!nav)return;nav.innerHTML=featureNavMarkup();
  document.querySelectorAll('#feature-nav [data-view]').forEach(button=>button.onclick=()=>{location.hash='#/'+button.dataset.feature;changeView(button.dataset.view);});
  const wanted=(location.hash||'').replace('#/','');const hit=features.find(f=>f.id===wanted&&!f.parentId&&f.id!=='my-campaigns');
  if(hit)changeView(hit.id==='content-library'?'content-library':'feature:'+hit.id);
}
function renderFeature(id){
  const f=features.find(item=>item.id===id);
  if(!f){$('#content').innerHTML='<div class="empty">This feature is not registered.</div>';return;}
  const children=features.filter(item=>item.parentId===f.id),deps=(f.dependencyIds||[]).map(d=>(features.find(x=>x.id===d)||{label:d}).label);
  $('#content').innerHTML=`<article class="panel planned-feature" data-feature-page="${esc(f.id)}"><span class="eyebrow">${esc((LIFECYCLE_LABEL[f.lifecycle]||f.lifecycle).toUpperCase())}</span><h2>${esc(f.label)}</h2><p>${esc(f.description)}</p><p class="note">This route is reserved. It has no live backend, so it shows no totals, records, listings or balances. Using it changes no saved campaign.</p>${deps.length?`<p class="note">Depends on: ${esc(deps.join(', '))}</p>`:''}${children.length?`<h3>Planned sections</h3>${children.map(c=>`<div class="list-row"><div><strong>${esc(c.label)}</strong><small>${esc(c.description)}</small></div><span class="badge">${esc(LIFECYCLE_LABEL[c.lifecycle]||c.lifecycle)}</span></div>`).join('')}`:''}</article>`;
}
async function renderContentLibrary(){
  $('#content').innerHTML='<div class="empty">Loading the Content Library…</div>';
  try{
    const data=await api('content-library',undefined,{creator:false});if(view!=='content-library')return;
    $('#content').innerHTML=data.campaigns.map(c=>`<article class="panel library-campaign" data-campaign="${esc(c.id)}"><span class="eyebrow">CAMPAIGN · ${esc(c.period)}</span><h2>${esc(c.title)}</h2><p>${esc(c.summary)}</p><p class="note">${esc(c.playable_entry_count)} of ${esc(c.entry_count)} entry points can start a playthrough today. The rest are proposed references.</p>${c.periods.map(p=>`<details class="period" ${p.entries.some(e=>e.playable)?'open':''}><summary>${esc(p.name)} · ${esc(p.range)}</summary>${p.entries.map(e=>`<div class="list-row"><div><strong>${esc(e.year)} · ${esc(e.title)}</strong><small>${esc(e.readiness)}</small></div>${e.playable?'<button class="primary" data-start-entry="'+esc(e.id)+'">Start new playthrough</button>':'<span class="badge">Proposed</span>'}</div>`).join('')}</details>`).join('')}</article>`).join('')+`<p class="note">${esc(data.note)}</p>`;
    document.querySelectorAll('[data-start-entry]').forEach(b=>b.onclick=()=>openCreateDialog());
  }catch(error){if(view==='content-library')$('#content').innerHTML=`<div class="empty">${esc(error.message)}</div>`;}
}
function syncComposer(){
  const player=workspaceMode==='player'&&current&&!loadingCampaign&&view==='story';$('#composer-form').hidden=!player;
  const accepted=current?.pending_declaration,allowed=Boolean(current?.capabilities?.can_declare)&&!accepted&&!transportPending;
  $('#send-declaration').disabled=busy||!player||!allowed||!$('#declaration').value.trim();
  $('#retry-action').hidden=!transportPending;$('#retry-action').disabled=busy;
  $('#withdraw-action').hidden=!accepted||Boolean(transportPending);$('#withdraw-action').disabled=busy;
  $('#composer-help').textContent=preferences.submitKey==='enter'?'Enter to submit · Shift+Enter for a new line':'Enter for a new line · Ctrl/Cmd+Enter to submit';
  $('#draft-state').textContent=$('#declaration').value?'Unsent draft · saved on this device':'Draft stays on this device';
  $('#action-state').textContent=busy?'Request in progress. You may inspect available records and edit an unsent draft.':transportPending?'Confirmation is pending. Check the saved request before submitting another attempt.':accepted?'Your exact declaration is persisted and awaiting resolution. Withdraw it explicitly before revising that pending intent.':!current?.actor_id?'A selected player character is required before declaring an action.':current.character_available===false?'The selected character is not currently available to act. Their identity and history are preserved; no replacement has been selected.':'A declaration records your intent. It does not imply an outcome or elapsed time.';
}
function storeTransport(pending){transportPending=pending;const key=pendingKey();if(key)writeLocal(key,pending);syncComposer();}
async function lookupAction(pending){return api('action-result/'+encodeURIComponent(pending.body.id)+'/'+encodeURIComponent(pending.body.request_id)+'?actor_id='+encodeURIComponent(pending.body.actor));}
async function finishAction(pending,result){
  if(current?.id!==pending.body.id||current?.actor_id!==pending.body.actor)return;
  storeTransport(null);if(pending.endpoint==='declaration'&&$('#declaration').value===pending.body.declaration){$('#declaration').value='';stashDraft();}
  await openCampaign(pending.body.id,{actorId:pending.body.actor});
  notice(result.status==='withdrawn'?'Pending intent withdrawn. The original declaration remains in the record.':'Declaration persisted exactly as submitted. It is awaiting resolution.');
}
async function deliverAction(pending,checkFirst=false){
  if(busy)return;setBusy(true);
  try{
    if(checkFirst){try{const found=await lookupAction(pending);await finishAction(pending,found);return;}catch(error){if(error.status!==404)throw error;}}
    try{const result=await api(pending.endpoint,pending.body,{creator:false});await finishAction(pending,result);}
    catch(error){
      try{const found=await lookupAction(pending);await finishAction(pending,found);}
      catch(checkError){
        if(checkError.status===404&&error.status&&error.status<500){storeTransport(null);await openCampaign(pending.body.id,{actorId:pending.body.actor});notice(error.message+' Your draft is retained.',true);}
        else{notice('The request may already be saved. Use Check / retry saved request to retrieve its result before any retry.',true);$('#connection-state').textContent='Confirmation pending · request identity retained';}
      }
    }
  }catch(error){notice(error.message,true);}finally{setBusy(false);}
}
async function submitDeclaration(){
  if(busy||!current?.capabilities?.can_declare||current.pending_declaration||transportPending)return;
  const declaration=$('#declaration').value;if(!declaration.trim())return;
  stashDraft();const pending={endpoint:'declaration',body:{id:current.id,revision:current.revision,request_id:crypto.randomUUID(),actor:current.actor_id,declaration}};storeTransport(pending);await deliverAction(pending);
}
async function withdrawDeclaration(){
  const action=current?.pending_declaration;if(busy||!action||transportPending)return;
  const pending={endpoint:'withdraw-declaration',body:{id:current.id,revision:current.revision,request_id:crypto.randomUUID(),actor:current.actor_id,action_request_id:action.request_id}};storeTransport(pending);await deliverAction(pending);
}
function applyPreferences(){
  preferences.theme=['dark','light','parchment'].includes(preferences.theme)?preferences.theme:'parchment';preferences.font=preferences.font==='sans'?'sans':'serif';
  preferences.fontSize=Math.max(16,Math.min(26,Number(preferences.fontSize)||18));preferences.lineHeight=Math.max(1.4,Math.min(2.2,Number(preferences.lineHeight)||1.8));preferences.width=Math.max(560,Math.min(1000,Number(preferences.width)||740));
  document.body.dataset.reading=preferences.theme;document.body.dataset.motion=preferences.motion==='reduce'?'reduce':'system';document.body.dataset.mechanics=preferences.mechanics==='expanded'?'expanded':'concise';
  document.documentElement.style.setProperty('--reading-font',preferences.font==='serif'?'Georgia, Cambria, serif':'"Segoe UI", system-ui, sans-serif');document.documentElement.style.setProperty('--reading-size',preferences.fontSize+'px');document.documentElement.style.setProperty('--reading-line',preferences.lineHeight);document.documentElement.style.setProperty('--reading-width',preferences.width+'px');
  $('#font-size-value').textContent=preferences.fontSize+' px';$('#line-height-value').textContent=preferences.lineHeight;$('#reading-width-value').textContent=preferences.width+' px';writeLocal('irgs-reading-preferences',preferences);syncComposer();
}
function openSettings(){for(const [key,value] of Object.entries(preferences)){const control=$('#preferences-form').elements.namedItem(key);if(control)control.value=value;}applyPreferences();$('#preferences-dialog').showModal();}
async function ensureCatalog(){if(!rows(library.campaign_profiles).length)library=await api('catalog');return library;}
async function renderTrash(){
  $('#content').innerHTML='<div class="empty">Loading Campaign Trash…</div>';
  try{const data=await api('trash');if(view!=='trash')return;$('#content').innerHTML=`<article class="panel"><span class="eyebrow">RECOVERABLE CAMPAIGNS</span><h2>${data.campaigns.length} campaign${data.campaigns.length===1?'':'s'} in Trash</h2><p>Restore returns the exact saved campaign, including its history and pending decisions.</p>${data.campaigns.map(campaign=>`<div class="list-row trash-row"><div><strong>${esc(campaign.name)}</strong><small>Revision ${esc(campaign.revision)}</small></div><button class="quiet" data-restore="${esc(campaign.id)}" data-revision="${campaign.revision}">Restore campaign</button></div>`).join('')||'<p class="note">Trash is empty.</p>'}</article>`;document.querySelectorAll('[data-restore]').forEach(button=>button.onclick=async()=>{if(busy)return;setBusy(true);try{const result=await api('restore',{id:button.dataset.restore,revision:Number(button.dataset.revision)});await refreshList(result.id);view='story';await openCampaign(result.id);notice('Campaign restored with its original save.');}catch(error){notice(error.message,true);}finally{setBusy(false);}});}catch(error){notice(error.message,true);}
}
function validHistoricalPreview() {
  return !historicalLoading && historicalPreview?.ready===true && Boolean(historicalPreview.snapshot)
    && historicalPreview.entry?.id===historicalEntryId && historicalPreview.request===historicalRequest
    && typeof historicalPreview.snapshot_sha256==='string' && /^[a-f0-9]{64}$/i.test(historicalPreview.snapshot_sha256);
}
function resetHistoricalSetup() {
  historicalRequest+=1;historicalEntryId=null;historicalPreview=null;historicalLoading=false;
  $('#historical-setup').hidden=true;$('#create-dialog').classList.toggle('historical-mode',false);syncCreateControls();
}
function historicalRequestCurrent(request,id) {return request===historicalRequest && $('#create-profile').value==='__hyw' && $('#create-dialog').open && (!id || historicalEntryId===id);}
function bindHistoricalButtons(selector) {
  document.querySelectorAll(selector).forEach(button=>{button.onclick=()=>{if(!busy)selectHistoricalEntry(button.dataset.historicalEntry);};});
}
function renderHistoricalChoices() {
  const entries=historicalCatalogue.entries || [],featured=historicalCatalogue.featured_years || [];
  $('#historical-featured').innerHTML=featured.map(year=>entries.find(entry=>String(entry.year)===String(year))).filter(Boolean).map(entry=>`<button type="button" class="quiet year-choice" data-historical-entry="${esc(entry.id)}" aria-pressed="false" title="${esc(entry.title)}">${esc(entry.year)}</button>`).join('');
  $('#historical-count').textContent=`All ${entries.length} entry points`;
  const draw=()=>{
    const query=$('#historical-search').value.trim().toLowerCase();
    const filtered=entries.filter(entry=>`${entry.year} ${entry.title || ''} ${entry.description || ''} ${entry.period_id || ''}`.toLowerCase().includes(query));
    $('#historical-all').innerHTML=filtered.map(entry=>`<button type="button" class="historical-entry" data-historical-entry="${esc(entry.id)}" aria-pressed="${entry.id===historicalEntryId}"><strong>${esc(entry.year)} · ${esc(entry.title)}</strong><small>${entry.status==='developed_historical_setup'?'Developed opening reference':'Proposed entry · snapshot pending'}</small></button>`).join('') || '<p class="note">No matching entry points.</p>';
    bindHistoricalButtons('#historical-all [data-historical-entry]');syncCreateControls();
  };
  $('#historical-search').value='';$('#historical-search').oninput=draw;$('#historical-search').onkeydown=event=>{if(event.key==='Enter')event.preventDefault();};draw();bindHistoricalButtons('#historical-featured [data-historical-entry]');
}
async function showHistoricalSetup() {
  const request=++historicalRequest;historicalEntryId=null;historicalPreview=null;historicalLoading=true;
  $('#historical-setup').hidden=false;$('#create-dialog').classList.toggle('historical-mode',true);
  $('#historical-preview').innerHTML='<p class="note">Loading historical entry points…</p>';syncCreateControls();
  try {
    const catalogue=historicalCatalogue || await api('historical-campaigns');
    if(!historicalRequestCurrent(request))return false;
    historicalCatalogue=catalogue;renderHistoricalChoices();
    const preferred=catalogue.entries.find(entry=>entry.id==='hyw-1415');
    if(!preferred)throw new Error('The developed 1415 entry is unavailable in this catalogue.');
    return await selectHistoricalEntry(preferred.id);
  } catch(err) {
    if(historicalRequestCurrent(request)){historicalLoading=false;$('#historical-preview').innerHTML=`<p class="note">${esc(err.message)}</p>`;syncCreateControls();}
    return false;
  }
}
async function selectHistoricalEntry(id,preserveError=false) {
  if(busy || $('#create-profile').value!=='__hyw' || !$('#create-dialog').open)return false;
  if(!(historicalCatalogue?.entries || []).some(entry=>entry.id===id))return false;
  const request=++historicalRequest;historicalEntryId=id;historicalPreview=null;historicalLoading=true;startingOptions=null;reviewSelection=null;startingRequest+=1;
  if(!preserveError)$('#create-error').textContent='';
  document.querySelectorAll('[data-historical-entry]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.historicalEntry===id)));
  $('#historical-preview').innerHTML='<p class="note">Loading the selected opening reference…</p>';syncCreateControls();
  try {
    const result=await api('historical-entry/'+encodeURIComponent(id));
    if(!historicalRequestCurrent(request,id))return false;
    if(result.entry?.id!==id)throw new Error('Historical entry identity mismatch. Select the entry again.');
    historicalPreview={...result,request};historicalLoading=false;
    const entry=result.entry;
    $('#historical-preview').innerHTML=`<article class="historical-preview"><div class="eyebrow">${esc(entry.year)} ENTRY POINT</div><h3>${esc(entry.title)}</h3><p>${esc(entry.description || '')}</p>${result.snapshot?historicalSnapshotMarkup(result.snapshot):'<p class="reference-note">Opening date and detailed snapshot not yet verified. This is catalogue reference material; campaign creation remains unavailable for this entry.</p>'}${validHistoricalPreview()?'<p class="ready-note">Opening snapshot available. Review the reference, choose your character, and confirm the campaign before it is saved.</p>':'<p class="note">This entry is available for inspection. A ready, verified opening snapshot is required for creation.</p>'}</article>`;
    syncCreateControls();return true;
  } catch(err) {
    if(historicalRequestCurrent(request,id)){historicalLoading=false;historicalPreview=null;$('#historical-preview').innerHTML=`<p class="note">${esc(err.message)}</p>`;syncCreateControls();}
    return false;
  }
}

function wizardBase(){
  const profile=$('#create-profile').value;
  if(profile!=='__hyw')return {profile_id:profile};
  if(!validHistoricalPreview())throw new Error('Choose a ready, verified opening snapshot before continuing.');
  return {profile_id:'military',scenario_id:'hundred-years-war',entry_id:historicalEntryId,snapshot_sha256:historicalPreview.snapshot_sha256};
}
function setupOriginKey(){try{return JSON.stringify(wizardBase());}catch{return null;}}
function validStartingOptions(){return !startingLoading&&startingOptions?.available===true&&startingOptions.queryKey===setupOriginKey()&&startingOptions.request===startingRequest&&startingOptions.default_scenario_id===$('#starting-scenario').value&&/^[a-f0-9]{64}$/i.test(startingOptions.selection_digest||'');}
function invalidateReview(){reviewSelection=null;}
function syncCreateControls(){
  const historical=$('#create-profile').value==='__hyw',pendingReview=Boolean(reviewSelection?.recovery);
  $('#create-profile').disabled=busy;$('#cancel-create').disabled=busy;$('#historical-search').disabled=busy;
  document.querySelectorAll('#historical-setup button').forEach(button=>button.disabled=busy);
  document.querySelectorAll('[data-setup-step]').forEach(section=>section.hidden=Number(section.dataset.setupStep)!==wizardStep);
  document.querySelectorAll('#setup-progress li').forEach((item,index)=>{if(index===wizardStep)item.setAttribute('aria-current','step');else item.removeAttribute('aria-current');});
  $('#setup-back').hidden=wizardStep===0||pendingReview;$('#setup-back').disabled=busy;
  $('#setup-next').hidden=wizardStep===3;$('#setup-next').disabled=busy||(wizardStep===1&&historical&&!validHistoricalPreview())||(wizardStep===2&&!validStartingOptions());
  $('#setup-next').textContent=wizardStep===0?'Choose starting point →':wizardStep===1?'Choose character →':'Review campaign →';
  $('#create-submit').hidden=wizardStep!==3;$('#create-submit').disabled=busy||wizardStep!==3||!reviewSelection;$('#create-submit').textContent=pendingReview?'Check / retry campaign creation':'Start campaign';
}
function setupDescriptionMarkup(description){
  if(!description)return '';
  if(typeof description==='string')return `<p>${esc(description)}</p>`;
  if(description.entry_guide)return entryGuideMarkup(description.entry_guide);
  if(description.immediate_situation||description.player_options||description.practical_pressures)return entryGuideMarkup(description);
  return textItems(description.summary||description.briefing||description.description).map(text=>`<p>${esc(text)}</p>`).join('');
}
function entryGuideMarkup(guide){
  if(!guide)return '';
  return `<section class="entry-guide"><h3>Before you start</h3>${textItems(guide.summary).map(text=>`<p>${esc(text)}</p>`).join('')}${[['immediate_situation','The immediate situation'],['player_options','Ways to enter this world'],['practical_pressures','Practical pressures'],['not_yet_established','What still needs to be established']].map(([key,title])=>textItems(guide[key]).length?`<details><summary>${title}</summary>${textItems(guide[key]).map(text=>`<p>${esc(text)}</p>`).join('')}</details>`:'').join('')}${guide.future_rule?`<p class="reference-note">${esc(guide.future_rule)}</p>`:''}</section>`;
}
function startingCharacters(){return startingOptions?.characters||startingOptions?.entities?.characters||[];}
function startingFactions(){return startingOptions?.factions||startingOptions?.entities?.factions||[];}
function factionRepresentatives(faction){return Array.isArray(faction?.control?.actor_ids)?startingCharacters().filter(character=>character.exists===true&&faction.control.actor_ids.includes(character.id)):[];}
function eligibleFactions(){return startingFactions().filter(faction=>faction.eligible===true&&factionRepresentatives(faction).length);}
async function loadStartingOptions(scenarioId=null){
  let base;try{base=wizardBase();}catch(error){$('#create-error').textContent=error.message;return;}
  const key=JSON.stringify(base),request=++startingRequest,priorKind=$('#character-kind').value,priorActor=$('#starting-character').value,priorFaction=$('#starting-faction').value;
  startingLoading=true;startingOptions=null;reviewSelection=null;$('#starting-context').innerHTML='<p>Loading dated character and faction availability…</p>';syncCreateControls();
  try{
    const result=await api('starting-options?'+new URLSearchParams({...base,...(scenarioId?{starting_scenario_id:scenarioId}:{})}).toString());
    if(request!==startingRequest||setupOriginKey()!==key||!$('#create-dialog').open)return;
    if(result.available!==true)throw new Error(result.reason||'No verified starting configuration is available.');
    startingOptions={...result,queryKey:key,request};startingLoading=false;
    const scenarios=result.scenarios||[],characters=result.characters||result.entities?.characters||[],factions=result.factions||result.entities?.factions||[],eligible=characters.filter(character=>character.eligible===true);
    $('#starting-context').innerHTML=`<span class="eyebrow">SOLO STARTING OPTIONS</span><h3>${esc(result.as_of?.label||'Profile setup')}</h3><p class="note">Availability comes from this selected starting point. Existence and participation do not grant player control.</p>${setupDescriptionMarkup(result.entry_description)}`;
    $('#starting-scenario').innerHTML=scenarios.map(scenario=>`<option value="${esc(scenario.id)}">${esc(scenario.title)}</option>`).join('');$('#starting-scenario').value=result.default_scenario_id||scenarios[0]?.id||'';
    const factionChoices=eligibleFactions();
    $('#character-kind').innerHTML=`${result.character_creation_allowed?'<option value="new">Create your own character</option>':''}${eligible.length?'<option value="existing">Choose an eligible existing character</option>':''}${factionChoices.length?'<option value="faction">Choose a policy-authorized faction</option>':''}`;
    $('#starting-character').innerHTML=characters.map(character=>`<option value="${esc(character.id)}" ${character.eligible?'':'disabled'}>${esc(character.name)}${character.eligible?'':' · unavailable'}</option>`).join('');
    $('#starting-character').value=eligible.some(character=>character.id===priorActor)?priorActor:eligible.find(character=>character.id==='AST-01')?.id||eligible[0]?.id||'';
    $('#starting-faction').innerHTML=factionChoices.map(faction=>`<option value="${esc(faction.id)}">${esc(faction.name)}</option>`).join('');$('#starting-faction').value=factionChoices.some(faction=>faction.id===priorFaction)?priorFaction:factionChoices[0]?.id||'';
    $('#character-kind').value=base.profile_id==='ast'&&eligible.some(character=>character.id==='AST-01')?'existing':priorKind==='faction'&&factionChoices.some(faction=>faction.id===priorFaction)?'faction':priorKind==='existing'&&eligible.some(character=>character.id===priorActor)?'existing':result.character_creation_allowed?'new':eligible.length?'existing':factionChoices.length?'faction':'';
    $('#starting-factions').innerHTML=factions.map(faction=>`<article class="record-card"><h3>${esc(faction.name)}</h3><p class="faction-state">Exists: ${faction.exists===true?'yes':faction.exists===false?'no':'unknown'} · Participation: ${esc(label(faction.participation||'unknown'))} · Control eligible: ${faction.eligible?'yes':'no'}</p><p class="note">${esc(faction.eligibility_reason||'Control requires a sourced policy.')}</p></article>`).join('')||'<p class="note">No dated faction records are supplied for this setup. New institutions must be established through the selected rules.</p>';
    updateCharacterFields();syncCreateControls();
  }catch(error){if(request===startingRequest){startingLoading=false;startingOptions=null;$('#starting-context').innerHTML=`<p class="reference-note">${esc(error.message)}</p>`;syncCreateControls();}}
}
function updateCharacterFields(){
  const kind=$('#character-kind').value,isNew=kind==='new';$('#new-character-fields').hidden=!isNew;$('#existing-character-fields').hidden=kind!=='existing';$('#faction-character-fields').hidden=kind!=='faction';
  for(const id of ['new-character-name','new-character-species','new-character-background'])$('#'+id).disabled=!isNew;
  $('#new-character-name').required=isNew;$('#new-character-species').required=isNew;
  const character=(startingOptions?.characters||startingOptions?.entities?.characters||[]).find(item=>item.id===$('#starting-character').value);
  $('#character-eligibility').textContent=character?.eligibility_reason||'Only an eligible individual can be selected.';updateFactionFields();invalidateReview();
}
function updateFactionFields(){
  const faction=eligibleFactions().find(item=>item.id===$('#starting-faction').value),prior=$('#faction-representative').value,representatives=factionRepresentatives(faction);
  $('#faction-representative').innerHTML=representatives.map(character=>`<option value="${esc(character.id)}">${esc(character.name)}</option>`).join('');$('#faction-representative').value=representatives.some(character=>character.id===prior)?prior:representatives[0]?.id||'';
  $('#faction-control-policy').innerHTML=faction?`${facts({control_mode:faction.control.mode,permitted_powers:faction.control.powers?.join(', ')||'None supplied',policy_reason:faction.eligibility_reason||'As recorded',policy_source:faction.eligibility_source_ref||'Not supplied'})}<p class="note">Only this policy’s listed powers apply through its permitted representative. Institutional commands still require their actual authority and resources.</p>`:'No eligible faction with a permitted existing representative is available.';invalidateReview();
}
function selectedCharacter(){
  if(!validStartingOptions())throw new Error('Refresh the verified starting options before reviewing this campaign.');
  if($('#character-kind').value==='existing'){
    const character=(startingOptions.characters||startingOptions.entities?.characters||[]).find(item=>item.id===$('#starting-character').value&&item.eligible===true);
    if(!character)throw new Error('Choose an eligible existing character.');return {kind:'existing',actor_id:character.id};
  }
  if($('#character-kind').value==='faction'){
    const faction=eligibleFactions().find(item=>item.id===$('#starting-faction').value),actor=$('#faction-representative').value;
    if(!faction||!factionRepresentatives(faction).some(character=>character.id===actor))throw new Error('Choose an eligible faction and its explicitly permitted existing representative.');
    return {kind:'faction',entity_id:faction.id,actor_id:actor};
  }
  if($('#character-kind').value!=='new')throw new Error('Choose a permitted player character or control policy.');
  if(!startingOptions.character_creation_allowed)throw new Error('Character creation is unavailable for this starting point.');
  const name=$('#new-character-name').value.trim(),species=$('#new-character-species').value.trim();if(!name||!species)throw new Error('Enter the character’s name and species.');
  return {kind:'new',name,species,background:$('#new-character-background').value};
}
function reviewedChoice(){
  const name=$('#campaign-name').value.trim();if(!name)throw new Error('Name the campaign before continuing.');
  const scenario=$('#starting-scenario').value;if(!(startingOptions?.scenarios||[]).some(item=>item.id===scenario))throw new Error('Choose an available solo scenario.');
  return {...wizardBase(),name,starting_scenario_id:scenario,selection_digest:startingOptions.selection_digest,character:selectedCharacter()};
}
function renderReview(payload,recovery=false){
  const character=payload.character||{},existing=startingCharacters().find(item=>item.id===character.actor_id),faction=startingFactions().find(item=>item.id===character.entity_id);
  const characterName=character.kind==='new'?character.name:existing?.name||character.actor_id;
  const control=character.kind==='new'?{mode:'individual',powers:['declare_own_intent']}:(character.kind==='faction'?faction:existing)?.control;
  const summary={profile:payload.scenario_id==='hundred-years-war'?'The Hundred Years’ War':label(payload.profile_id),starting_point:startingOptions?.as_of?.label||payload.entry_id||'Profile checkpoint',character:characterName,species:character.species||existing?.species||existing?.identity?.species||'as recorded',scenario:payload.starting_scenario_id||'individual',...(character.kind==='faction'?{faction:faction?.name||character.entity_id}:{}),control_mode:control?.mode?label(control.mode):'Policy terms not loaded',permitted_powers:Array.isArray(control?.powers)?control.powers.join(', ')||'None supplied':'Not loaded; the retained selection will be checked by the host'};
  $('#setup-review').innerHTML=`<span class="eyebrow">SOLO CAMPAIGN REVIEW</span><h2>${esc(payload.name)}</h2>${recovery?'<p class="reference-note">A previous Start request has an unconfirmed receipt. Retry this exact request to recover the same campaign. Its identity and choices are retained.</p>':''}<div class="setup-summary">${facts(summary)}</div>${character.kind==='faction'&&faction?`<p class="note">${esc(faction.eligibility_reason||'As recorded in the selected control policy.')}</p>${facts({control_policy_source:faction.eligibility_source_ref||'Not supplied'})}`:''}${character.kind==='new'&&character.background?`<h3>User-declared background</h3><p class="record">${esc(character.background)}</p><p class="note">This declaration supplies background testimony; capabilities and possessions require their own established records.</p>`:''}${setupDescriptionMarkup(startingOptions?.entry_description)}<p class="reference-note">${character.kind==='faction'?'Faction selection grants only the reviewed policy’s listed powers through the permitted representative. It supplies no automatic national authority, appointments or resources.':'The selected person’s control follows the listed policy. Wealth, inventory quantities, capabilities, appointments and faction-level powers remain unknown unless the selected profile supplies them.'}</p><details><summary>Starting reference provenance</summary>${facts({source:startingOptions?.source||'Retained creation request',selection_digest:payload.selection_digest,snapshot_sha256:payload.snapshot_sha256||'Not a historical snapshot'})}</details>`;
}

function creationPayload(){
  if(wizardStep!==3||!reviewSelection)throw new Error('Review the campaign and character before starting.');
  if(!reviewSelection.recovery&&JSON.stringify(reviewedChoice())!==reviewSelection.signature)throw new Error('The starting choices changed. Review them again before starting.');
  reviewSelection.requestId=reviewSelection.requestId||crypto.randomUUID();return {...reviewSelection.payload,request_id:reviewSelection.requestId};
}
async function wizardNext(){
  if(busy)return;$('#create-error').textContent='';
  try{
    if(wizardStep===0){if(!$('#campaign-name').value.trim())throw new Error('Enter a campaign name.');wizardStep=1;invalidateReview();if($('#create-profile').value==='__hyw')await showHistoricalSetup();else{$('#profile-opening').innerHTML=$('#create-profile').value==='ast'?'<h3>A Scot’s Tale · confirmed checkpoint</h3><p>The existing post-Day-2 guide is retained. Ian’s next action remains undeclared. Existing campaign saves are separate from this new playthrough.</p>':'<h3>A new, sourced campaign</h3><p>No historical date is inferred for this generic profile. Create a character next; actual possessions and capabilities remain to be established.</p>';}}
    else if(wizardStep===1){wizardBase();wizardStep=2;await loadStartingOptions();}
    else if(wizardStep===2){const payload=reviewedChoice();reviewSelection={payload,signature:JSON.stringify(payload),requestId:null};wizardStep=3;renderReview(payload);}
    syncCreateControls();$('#create-title').focus?.();
  }catch(error){$('#create-error').textContent=error.message;syncCreateControls();}
}
async function openCreateDialog(){
  if(busy||!token)return;$('#create-error').textContent='';try{await ensureCatalog();loadProfiles();const pending=readLocal('irgs-create-pending');if(pending){wizardStep=3;reviewSelection={payload:pending,requestId:pending.request_id,recovery:true};renderReview(pending,true);}else{wizardStep=0;reviewSelection=null;startingOptions=null;$('#campaign-name').value='';$('#new-character-name').value='';$('#new-character-species').value='human';$('#new-character-background').value='';}$('#create-dialog').showModal();syncCreateControls();}catch(error){notice(error.message,true);}
}
function loadProfiles(){
  const profiles=rows(library.campaign_profiles).filter(profile=>!['hundred-years-war','hyw'].includes(profile.id)&&profile.scenario_id!=='hundred-years-war');
  $('#create-profile').innerHTML=profiles.map(profile=>`<option value="${esc(profile.id)}">${esc(profile.name||profile.id)}</option>`).join('')+'<option value="__hyw">The Hundred Years’ War · historical campaign library</option>';if(profiles.some(profile=>profile.id==='ast'))$('#create-profile').value='ast';
  const describe=()=>{startingRequest+=1;startingOptions=null;reviewSelection=null;wizardStep=0;resetHistoricalSetup();$('#profile-opening').innerHTML='';const profile=profiles.find(item=>item.id===$('#create-profile').value);$('#profile-description').textContent=$('#create-profile').value==='__hyw'?'The Military genre with a verified dated opening. Choose the start, then your solo character.':profile?.description||profile?.initial_state||profile?.source_status||'';syncCreateControls();};
  $('#create-profile').onchange=describe;describe();
}
document.querySelectorAll('[data-view]').forEach(button=>button.onclick=()=>changeView(button.dataset.view));
document.querySelectorAll('[role=tab]').forEach(button=>button.onkeydown=event=>{if(!['ArrowLeft','ArrowRight','Home','End'].includes(event.key))return;event.preventDefault();const tabs=[...document.querySelectorAll('[role=tab]')],index=tabs.indexOf(button),next=event.key==='Home'?0:event.key==='End'?tabs.length-1:(index+(event.key==='ArrowRight'?1:-1)+tabs.length)%tabs.length;changeView(tabs[next].dataset.view);tabs[next].focus();});
bindInspectors();$('#close-inspector').onclick=()=>$('#inspect-dialog').close();
$('#toggle-nav').onclick=()=>{const open=document.body.classList.toggle('nav-open');$('#toggle-nav').setAttribute('aria-expanded',String(open));};
$('#toggle-context').onclick=()=>{const open=document.body.classList.toggle('context-open');$('#toggle-context').setAttribute('aria-expanded',String(open));if(open)$('#close-context').focus();};
$('#close-context').onclick=()=>{document.body.classList.remove('context-open');$('#toggle-context').setAttribute('aria-expanded','false');$('#toggle-context').focus();};
document.addEventListener('keydown',event=>{if(event.key!=='Escape'||document.querySelector('dialog[open]'))return;if(document.body.classList.contains('context-open')){$('#close-context').click();event.preventDefault();}else if(document.body.classList.contains('nav-open')){document.body.classList.remove('nav-open');$('#toggle-nav').setAttribute('aria-expanded','false');$('#toggle-nav').focus();event.preventDefault();}});
$('#settings').onclick=openSettings;$('#close-settings').onclick=()=>$('#preferences-dialog').close();$('#preferences-form').onsubmit=event=>event.preventDefault();
$('#preferences-form').oninput=event=>{const control=event.target;if(control.name){preferences[control.name]=control.type==='range'?Number(control.value):control.value;applyPreferences();document.querySelectorAll('.mechanical-detail').forEach(detail=>detail.open=preferences.mechanics==='expanded');}};
$('#declaration').oninput=()=>{stashDraft();syncComposer();};$('#declaration').onkeydown=event=>{const submit=event.key==='Enter'&&(preferences.submitKey==='enter'?!event.shiftKey:(event.ctrlKey||event.metaKey));if(submit){event.preventDefault();if(!$('#send-declaration').disabled)$('#composer-form').requestSubmit();}};
$('#composer-form').onsubmit=event=>{event.preventDefault();submitDeclaration();};$('#retry-action').onclick=()=>{if(transportPending)deliverAction(transportPending,true);};$('#withdraw-action').onclick=withdrawDeclaration;
$('#campaign').onchange=()=>{if(busy){$('#campaign').value=current?.id||'';return;}openCampaign($('#campaign').value).catch(error=>notice(error.message,true));};
$('#player-character').onchange=()=>{if(busy){$('#player-character').value=current?.actor_id||'';return;}if(current)openCampaign(current.id,{actorId:$('#player-character').value}).catch(error=>notice(error.message,true));};
$('#workspace-mode').onclick=async()=>{
  if(busy)return;stashDraft();rememberScroll();const id=current?.id,actor=current?.actor_id;
  campaignRequest+=1;workspaceMode=workspaceMode==='creator'?'player':'creator';view=workspaceMode==='creator'?'creator':'story';current=null;currentBinding=null;transportPending=null;
  if($('#inspect-dialog').open)$('#inspect-dialog').close();$('#inspect-content').innerHTML='';render();
  const mode=workspaceMode,request=campaignRequest;
  try{if(mode==='creator')await ensureCatalog();if(request!==campaignRequest||workspaceMode!==mode||$('#campaign').value!==(id||''))return;if(id)await openCampaign(id,{actorId:actor});}catch(error){if(request===campaignRequest)notice(error.message,true);}
};
$('#new-campaign').onclick=openCreateDialog;$('#cancel-create').onclick=()=>{if(!busy)$('#create-dialog').close();};
$('#create-dialog').addEventListener('close',()=>{resetHistoricalSetup();startingRequest+=1;startingOptions=null;reviewSelection=null;});$('#create-dialog').addEventListener('cancel',event=>{if(busy)event.preventDefault();});
$('#setup-next').onclick=wizardNext;$('#setup-back').onclick=()=>{if(busy||wizardStep===0)return;if(readLocal('irgs-create-pending')){$('#create-error').textContent='Check the retained Start request before changing its choices.';return;}wizardStep-=1;invalidateReview();$('#create-error').textContent='';syncCreateControls();};
$('#character-kind').onchange=updateCharacterFields;$('#starting-character').onchange=updateCharacterFields;$('#starting-scenario').onchange=()=>loadStartingOptions($('#starting-scenario').value);$('#starting-faction').onchange=updateFactionFields;$('#faction-representative').onchange=invalidateReview;
for(const id of ['new-character-name','new-character-species','new-character-background','campaign-name'])$('#'+id).oninput=invalidateReview;
$('#create-form').onsubmit=async event=>{
  event.preventDefault();if(busy||wizardStep!==3)return;let payload;
  try{payload=creationPayload();}catch(error){$('#create-error').textContent=error.message;return;}
  writeLocal('irgs-create-pending',payload);setBusy(true);$('#create-error').textContent='';
  try{const record=await api('create',payload,{creator:false});
    if(record.status==='trashed'){writeLocal('irgs-create-pending',null);$('#create-dialog').close();view='trash';render();notice('This Start request already created a campaign that is now in Trash. Restore it there.');return;}
    await refreshList(record.id);workspaceMode='player';view='story';await openCampaign(record.id);writeLocal('irgs-create-pending',null);$('#create-dialog').close();notice('Campaign started with the character and starting choices you reviewed.');
  }catch(error){notice(error.message,true);$('#create-error').textContent=error.message;
    if(error.status===400){writeLocal('irgs-create-pending',null);reviewSelection=null;startingOptions=null;wizardStep=1;$('#create-error').textContent=error.message+' Review a fresh starting point and character selection.';if($('#create-profile').value==='__hyw'&&historicalEntryId){setBusy(false);await selectHistoricalEntry(historicalEntryId,true);setBusy(true);}}
    else if(reviewSelection){reviewSelection.recovery=true;renderReview(payload,true);}
  }finally{setBusy(false);}
};
$('#fork').onclick=async()=>{if(workspaceMode!=='creator'||!current||busy||loadingCampaign)return;const id=current.id;setBusy(true);try{const branch=await api('fork',{id});await refreshList(branch.id);await openCampaign(branch.id);notice('Independent campaign branch saved.');}catch(error){notice(error.message,true);}finally{setBusy(false);}};
$('#delete-campaign').onclick=()=>{if(!current||busy||loadingCampaign||$('#campaign').value!==current.id)return;deleteTarget={id:current.id,revision:current.revision,name:current.name,origin:current.state?.fork_origin?.save_id,request:campaignRequest};$('#delete-name').textContent=current.name;$('#delete-error').textContent='';$('#delete-dialog').showModal();};
$('#cancel-delete').onclick=()=>{if(!busy)$('#delete-dialog').close();};$('#delete-dialog').addEventListener('close',()=>{deleteTarget=null;});$('#delete-dialog').addEventListener('cancel',event=>{if(busy)event.preventDefault();});
$('#delete-form').onsubmit=async event=>{event.preventDefault();if(!deleteTarget||busy)return;const target=deleteTarget;if(loadingCampaign||current?.id!==target.id||$('#campaign').value!==target.id||campaignRequest!==target.request){$('#delete-dialog').close();notice('The visible campaign changed. Select it again before deleting.',true);return;}setBusy(true);try{await api('delete',{id:target.id,revision:target.revision});$('#delete-dialog').close();await openCampaign('');const campaigns=await refreshList(),next=campaigns.find(campaign=>campaign.id===target.origin)||campaigns[0];await openCampaign(next?.id||'');notice('Campaign moved to Trash. Its complete save can be restored.');}catch(error){$('#delete-error').textContent=error.message;}finally{setBusy(false);}};
$('#export').onclick=()=>{if(!current||busy||loadingCampaign)return;const full=workspaceMode==='creator'&&current.mode==='creator'&&current.state,data=full||current,blob=new Blob([JSON.stringify(data,null,2)],{type:'application/json'}),url=URL.createObjectURL(blob),link=document.createElement('a');link.href=url;link.download=`IRGS-${full?'full-save':'known-view'}-${current.id}-r${current.revision}.json`;link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);};
applyPreferences();syncControls();
(async()=>{try{const campaigns=await refreshList();const previous=localStorage.getItem('irgs-active'),id=campaigns.find(campaign=>campaign.id===previous)?.id||campaigns[0]?.id;if(id)await openCampaign(id);else render();}catch(error){notice('Cannot connect to the IRGS host: '+error.message,true);$('#content').innerHTML='<div class="empty">Start the local server and reload this page.</div>';}})();
(async()=>{try{await loadFeatureNav();}catch(error){}})();
