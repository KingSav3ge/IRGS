'use strict';
const $ = s => document.querySelector(s);
const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let token, current = null, view = 'session', busy = false;
const titles = {session:['Your world, in motion.','A place to play, observe, and test the IRGS system.'],characters:['The people in your world.','Character identities and confirmed state from the active game.'],ledger:['Every fact has a history.','Evidence, resources, and obligations in the current world.'],journal:['The record of what happened.','Accepted engine events, preserved in causal order.'],library:['One system. Many worlds.','IRGS is the top-level system. Games bring its Core and engines into play.']};
function notice(text, error = false) { $('#notice').textContent = text; $('#notice').className = error ? 'error' : ''; }
async function api(path, body) {
  const response = await fetch('/api/' + path, body ? {method:'POST',headers:{'Content-Type':'application/json','X-IRGS-Token':token},body:JSON.stringify(body)} : {});
  const result = await response.json(); if (!response.ok) throw new Error(result.error || 'Request failed'); return result;
}
async function refreshList(selected) {
  const data = await api('campaigns'); token = data.token;
  $('#campaign').innerHTML = '<option value="">Choose a campaign</option>' + data.campaigns.map(c=>`<option value="${c.id}">${esc(c.name)}</option>`).join('');
  if (selected) $('#campaign').value = selected;
  return data.campaigns;
}
async function openCampaign(id) {
  current = id ? await api('campaign/' + id) : null;
  if (current) localStorage.setItem('irgs-active', id);
  $('#export').disabled = $('#fork').disabled = !current;
  render();
}
function empty() { return `<div class="empty"><div class="eyebrow">WELCOME TO IRGS</div><h2>Your next world starts here.</h2><p>Create an AST beta-game campaign to test the IRGS Core and connected engine.<br>Each campaign gets its own persistent world state.</p><button class="primary" id="empty-create">Create your first campaign →</button></div>`; }
function render() {
  $('#page-title').textContent = titles[view][0]; $('#page-subtitle').textContent = titles[view][1];
  $('#section-label').textContent = view === 'session' ? 'CAMPAIGN ROOM' : view.toUpperCase();
  document.querySelectorAll('[data-view]').forEach(b=>b.classList.toggle('selected',b.dataset.view===view));
  $('#saved').textContent = current ? `Saved locally · revision ${current.revision}` : 'Local host connected';
  if (view === 'library') return renderLibrary();
  if (!current) { $('#content').innerHTML = empty(); $('#empty-create').onclick = ()=>$('#create-dialog').showModal(); return; }
  ({session:renderSession,characters:renderCharacters,ledger:renderLedger,journal:renderJournal})[view]();
}
const label = key => key.replaceAll('_',' ').replace(/\b\w/g,c=>c.toUpperCase());
function facts(obj) { return Object.entries(obj).map(([k,v])=>`<div class="list-row"><small>${esc(label(k))}</small><strong>${esc(typeof v === 'object' ? JSON.stringify(v) : v)}</strong></div>`).join('') || '<p>No confirmed records yet.</p>'; }
function renderSession() {
  const s = current.state, time = s.campaign_time;
  $('#content').innerHTML = `<div class="grid"><div><article class="panel scene"><div class="eyebrow">AST / BETA GAME · DAY ${esc(time.day)}</div><h2>${esc(current.name)}</h2><p>${esc(time.phase)}</p><span class="badge">${esc(time.time || 'Time not specified')}</span></article><div class="stats"><div class="stat"><small>CHARACTERS</small><strong>${Object.keys(s.actors).length}</strong></div><div class="stat"><small>EVENTS RECORDED</small><strong>${s.journal.length}</strong></div><div class="stat"><small>DECLARED ACTIONS</small><strong>${s.player_actions.length}</strong></div></div><article class="panel"><div class="eyebrow">PLAYER CHARACTER</div><h2>${esc(s.actors['AST-01'].name)}</h2>${facts(s.actors['AST-01'].current)}</article></div><div><article class="panel"><div class="eyebrow">YOUR NEXT MOVE</div><h2>Declare an action</h2><p class="note">Tell the game what your character attempts. The engine records the declaration; outcomes require established evidence.</p><form id="action-form"><label>What do you do?<textarea name="declaration" required maxlength="10000" placeholder="Describe your character’s intended action…"></textarea></label><label>Player instruction reference<input name="instruction_ref" required placeholder="e.g. Player declaration, session 1"></label><label>Source reference<input name="source_ref" required placeholder="e.g. Session 1, turn 1"></label><div class="buttons"><button class="primary">Record declaration →</button></div></form></article><article class="panel spacer"><div class="eyebrow">RECENT DECLARATIONS</div><h2>The story so far</h2>${s.player_actions.slice(-3).reverse().map(a=>`<div class="list-row"><strong>${esc(a.declaration)}</strong><small>Declared · awaiting resolution · sequence ${a.at}</small></div>`).join('') || '<p class="note">No player actions declared in this campaign yet. The confirmed checkpoint is intact.</p>'}</article></div></div><details><summary>Game host tools · scenes, evidence, inventory, and orders</summary><div id="host-tools" class="panel spacer"></div></details>`;
  $('#action-form').onsubmit = e => {e.preventDefault(); submit('ast_record_player_action', {...Object.fromEntries(new FormData(e.target)),actor:'AST-01'});};
  mountTools();
}
const operations = {
 ast_set_scene:['Set the scene',{day:'number',time:'text',precision:['approximate','exact','unknown'],description:'textarea',instruction_ref:'text'}],
 ast_record_evidence:['Record evidence',{evidence_id:'text',subject:'actor',assertion:'textarea',status:['established','testimony','inference','provisional','unknown','superseded']}],
 ast_receive_evidence:['Receive evidence',{evidence_id:'text',recipient:'actor'}],
 ast_confirm_character_field:['Confirm character state',{subject:'actor',evidence_id:'text',field:['location','condition','custody','service','current_activity'],value:'text',authority_ref:'text',instruction_ref:'text'}],
 ast_establish_stock:['Establish inventory',{location:'text',material:'text',quantity:'number',inventory_evidence_ref:'text'}],
 ast_transfer_stock:['Transfer inventory',{from:'text',to:'text',material:'text',quantity:'number',authority_ref:'text'}],
 ast_record_obligation:['Record an obligation',{obligation_id:'text',subject:'actor',description:'textarea',status:['offered','agreed','due','disputed','fulfilled','unknown'],instruction_ref:'text'}],
 ast_record_design:['Record a design',{design_id:'text',name:'text'}],
 ast_receive_order:['Receive an order',{order_id:'text',recipient:'actor',content:'textarea',authority_ref:'text'}]
};
function mountTools() {
  $('#host-tools').innerHTML = `<h2>Record a world event</h2><p class="note">Use these tools for explicit, sourced game-host decisions. Recording an order does not execute it; recording a design does not manufacture it.</p><label>Operation<select id="operation">${Object.entries(operations).map(([id,[name]])=>`<option value="${id}">${name}</option>`).join('')}</select></label><form id="event-form"><div id="fields"></div><label>Source reference<input name="source_ref" required placeholder="Source establishing this event"></label><div class="buttons"><button class="primary">Apply event</button></div></form>`;
  function fields() { $('#fields').innerHTML = Object.entries(operations[$('#operation').value][1]).map(([key,type])=>{
    let control;
    if (type === 'actor') control = `<select name="${key}">${Object.values(current.state.actors).map(a=>`<option value="${a.id}">${esc(a.name)} · ${a.id}</option>`).join('')}</select>`;
    else if (Array.isArray(type)) control = `<select name="${key}">${type.map(v=>`<option value="${v}">${label(v)}</option>`).join('')}</select>`;
    else if (type === 'textarea') control = `<textarea name="${key}" required maxlength="10000"></textarea>`;
    else control = `<input name="${key}" type="${type}" required ${type === 'number' ? 'min="0" step="1"' : 'maxlength="2000"'} ${key==='day' ? `value="${current.state.campaign_time.day}"` : ''}>`;
    return `<label>${label(key)}${control}</label>`;
  }).join(''); }
  fields(); $('#operation').onchange = fields;
  $('#event-form').onsubmit = e=>{e.preventDefault();const op=$('#operation').value,params=Object.fromEntries(new FormData(e.target));for(const [k,t] of Object.entries(operations[op][1])) if(t==='number') params[k]=Number(params[k]);submit(op,params);};
}
async function submit(op, params) {
  if (busy) return; busy = true;
  const buttons = [...$('#content').querySelectorAll('button')]; buttons.forEach(b=>b.disabled=true);
  try { current=await api('event',{id:current.id,revision:current.revision,op,params});render();notice('Event accepted by the IRGS engine and saved locally.'); }
  catch(err) { notice(err.message,true); }
  finally { busy=false;buttons.forEach(b=>b.disabled=false); }
}
function renderCharacters() {
  $('#content').innerHTML = `<div class="toolbar"><h2>Character registry <span class="badge">${Object.keys(current.state.actors).length} RECORDS</span></h2><input id="search" aria-label="Search characters" placeholder="Search names or roles…"></div><div class="cards" id="characters"></div>`;
  const draw=()=>{ const query=$('#search').value.toLowerCase();const actors=Object.values(current.state.actors).filter(a=>(a.name+' '+current.state.registry.characters[a.id].role).toLowerCase().includes(query));$('#characters').innerHTML=actors.map(a=>`<button class="character" data-actor="${a.id}"><span class="initial">${esc(a.name.split(' ').map(n=>n[0]).slice(0,2).join(''))}</span><strong>${esc(a.name)}</strong><small>${esc(current.state.registry.characters[a.id].role)}</small><small>${a.id} / ${esc(a.species)}</small></button>`).join('')||'<p>No matching characters.</p>';document.querySelectorAll('[data-actor]').forEach(b=>b.onclick=()=>showCharacter(b.dataset.actor));};
  $('#search').oninput=draw;draw();
}
function showCharacter(id) {
 const a=current.state.actors[id],r=current.state.registry.characters[id];
 $('#content').innerHTML=`<button id="back" class="quiet back">← All characters</button><div class="grid"><article class="panel"><div class="eyebrow">${a.id} / ${esc(a.species)}</div><h2>${esc(a.name)}</h2><p>${esc(r.role)}</p><h3>Confirmed current state</h3>${facts(a.current)}<h3 class="spacer">Received knowledge</h3>${facts(current.state.knowledge[id]||{})}</article><article class="panel"><h2>Registry guide</h2><p class="note">Reference material. Provisional ratings are not adopted by the runtime.</p>${r.record_text.map(t=>`<p class="record">${esc(t)}</p>`).join('')}</article></div>`;$('#back').onclick=renderCharacters;
}
function renderLedger() {
 const s=current.state;
 const rows=Object.entries(s.stocks).flatMap(([loc,items])=>Object.entries(items).map(([mat,q])=>`<tr><td>${esc(loc)}</td><td>${esc(mat)}</td><td>${q}</td></tr>`)).join('');
 $('#content').innerHTML=`<div class="grid"><article class="panel"><h2>Resources</h2>${rows?`<table><thead><tr><th>Location</th><th>Material</th><th>Quantity</th></tr></thead><tbody>${rows}</tbody></table>`:'<p>No inventory quantities established. Unknown quantities remain unknown.</p>'}<h2 class="spacer">Obligations</h2>${facts(s.obligations)}<h2 class="spacer">Designs</h2>${facts(s.designs)}</article><article class="panel"><h2>Evidence</h2>${Object.entries(s.evidence).map(([id,e])=>`<div class="list-row"><span class="badge">${esc(e.status)}</span><strong>${esc(e.assertion)}</strong><small>${esc(id)} · ${esc(s.actors[e.subject].name)}<br>Source: ${esc(e.source_ref)}</small></div>`).join('')||'<p>No evidence records yet.</p>'}<h2 class="spacer">Received orders</h2>${facts(s.orders)}</article></div>`;
}
function renderJournal() {
 const events=[...current.state.journal].reverse();
 $('#content').innerHTML=`<article class="panel"><div class="eyebrow">PERSISTENT EVENT HISTORY</div><h2>${events.length} recorded event${events.length===1?'':'s'}</h2>${events.length?events.map(e=>`<details><summary>Sequence ${e.at} · ${esc(label(e.op.replace('ast_','')))}</summary><p class="note">${esc(e.id)}</p><pre>${esc(JSON.stringify(e.params,null,2))}</pre></details>`).join(''):'<p>The campaign is at its initial checkpoint. Your first accepted event will appear here.</p>'}</article>`;
}
function renderLibrary() {
 $('#content').innerHTML=`<article class="panel scene"><div class="eyebrow">INTERACTIVE ROLEPLAYING GAMES SYSTEMS</div><h2>IRGS is the foundation.</h2><p>The Core defines shared rules and state. Engines provide domain behavior. Games and campaigns use those systems to create playable worlds.</p></article><div class="cards spacer"><article class="panel"><span class="badge">SYSTEM</span><h2>IRGS Core</h2><p>The top-level simulation foundation for engine rules, causal events, and world state.</p><small>Core selection is profile-specific. This host does not change global version adoption.</small></article><article class="panel"><span class="badge">CONNECTED BETA GAME</span><h2>AST</h2><p>The beta game for testing IRGS Core + engines. The first playable integration in this host uses the existing AST Core 3.3 runtime.</p><small>37 registered characters · sourced events · persistent campaigns</small></article><article class="panel"><span class="badge">SOURCE LIBRARY</span><h2>Other engines</h2><p>Roman Republic, Military, Fantasy, PAF, Shinobi Nexus, and Space Exploration sources are present in the workspace.</p><small>These engines need their own playable adapters before they can be launched here.</small></article></div>`;
}
document.querySelectorAll('[data-view]').forEach(b=>b.onclick=()=>{view=b.dataset.view;render();});
$('#new-campaign').onclick=()=>$('#create-dialog').showModal();$('#cancel-create').onclick=()=>$('#create-dialog').close();
$('#campaign').onchange=()=>openCampaign($('#campaign').value).catch(err=>notice(err.message,true));
$('#create-form').onsubmit=async e=>{e.preventDefault();const button=e.target.querySelector('.primary');button.disabled=true;try{const r=await api('create',{name:new FormData(e.target).get('name')});await refreshList(r.id);await openCampaign(r.id);$('#create-dialog').close();e.target.reset();notice('AST beta-game campaign created. Your world is ready.');}catch(err){notice(err.message,true);$('#create-dialog').close();}finally{button.disabled=false;}};
$('#fork').onclick=async()=>{if(!current||busy)return;busy=true;try{const r=await api('fork',{id:current.id});await refreshList(r.id);await openCampaign(r.id);notice('Campaign branched. Continue here to explore a different path.');}catch(err){notice(err.message,true);}finally{busy=false;}};
$('#export').onclick=()=>{if(!current)return;const blob=new Blob([JSON.stringify(current.state,null,2)],{type:'application/json'}),url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download=`IRGS-AST-${current.id}-r${current.revision}.json`;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);};
(async()=>{try{const campaigns=await refreshList();const previous=localStorage.getItem('irgs-active');const id=campaigns.find(c=>c.id===previous)?.id||campaigns[0]?.id; if(id){$('#campaign').value=id;await openCampaign(id);}else render();}catch(err){notice('Cannot connect to the IRGS host: '+err.message,true);$('#content').innerHTML='<div class="empty">Start the local server, then reload this page.</div>';}})();
