# Rise foundation 1

The user selected a clearly fictional first founding example, with shared setup for all eight design families. R00, Greywater Reach, is an authored demonstration. H01–H06, N01 and F01 have explicit held catalogue records; none has an executable opening. This increment does not complete M2–M7 or certify the specification's entire acceptance catalogue.

## Receiving and ownership

| Contract | Authoritative state / existing owner | Implemented scope |
| --- | --- | --- |
| Configuration | `rise`, `settlement_model` definitions | Exact reviewed choices, model, source and digest; no mutable quantities or population in Rise metadata |
| Identity | `actors` / K-ACTOR | Named founder, optional reviewed sibling or independent second household, known steward and neighbor; founder control only |
| People and membership | `households`, `migrations`, `settlements` / K-POP and K-ORG | Existing named people, separate household and camp membership, actual departure and arrival; no population counter |
| Authority | `organizations`, `grants` / K-ORG | Fictional limited issuer, separate offer and acceptance, current permission checks, preserved existing path |
| Goods | `stocks`, `opening_stock`, `stock_accounts`, `material_flows` / K-STOCK | One physical quantity; owned stores, reservations derived from active work, explicit consumption flows; opening = remaining + consumed |
| Time | `elapsed_time`, `provision.next_at` / K-TIME | Selected elapsed seconds, earliest completion/provision boundary; causal sequence and save revision remain separate |
| Work | `projects` / K-WORK | Finite one-worker shelter/repair recipes, actual tools and inputs, pause/resume, retained progress, no duplicate physical project |
| Structures | `assets`, `land_claims` / K-ASSET | Accepted shelter places, ownership and existing use; no free building at founding |
| Service and needs | Accepted asset capacity and `provision.assessments` / K-NET, K-WORK | Shelter shortfall and actual grain delivery/deficit; no implied injury or death model |
| Information | `settlement_receipts` / K-INFO | Recipient-scoped committed messages and local observations; remote private work and stocks excluded from player views |

These are namespace mappings within the nine existing owners. No owner is added. Mixed household, settlement and provision records require field-aware attribution; operation tooling leaves those broad records unmapped instead of inventing precision. Actual dependencies come from ordinary handler execution through R9 observation, not this table.

## Selected fictional procedures

Setup independently selects solo, adult sibling Rowan, or a second independent household; permission sought or already received/accepted; and basic or stocked supplies. Names, fictional region label and opening date label are editable. All material starting facts and numerical model values must be reviewed before initialization. No spouse, debt, political act, skills or additional voluntary history is generated. No save is migrated.

Travel takes 300 seconds. A shelter uses three prepared timber bundles, one serviceable axe as a retained tool and 3,600 seconds of one person's work, yielding two shelter places. Oren's independent standing repair uses one timber bundle and 1,800 seconds through the same work processor. One grain portion per household member is assessed every 21,600 seconds; two portions of the same stock are protected seed, not extra food. Deficits remain recorded without erasing people. Oren's agreed migration takes 900 seconds with existing private goods. Values are authored test and play procedures, uncalibrated and valid only for this selected demonstration.

The grant permits the founder's camp and temporary dwelling, including a consenting incoming household; it preserves the existing seasonal path and grants no forest use, taxation, government or supplies. Oren's invitation, agreement, departure and arrival remain distinct. The neighbor's single authored decision requires received camp information, completed repair and sufficient own provision. Joining conveys no player labor authority or ownership of private goods. The second starting household likewise retains private property and control.

Time advancement processes already authorized work and movement, with no new PC choices. A one-hour request returns earlier at the first meaningful process boundary. A selected five-minute walk processes intermediate boundaries and finishes the route. A paused project retains work but releases inputs; resumption rechecks means and permission. Revocation holds the dependent shelter work. Existing capacity bookings with no mapping to elapsed seconds hold the same worker instead of guessing a conversion.

## Support limits

This is one local host writing one save directory, using atomic file replacement and stable creation/action identities. It is not a distributed multiwriter protocol. The civil calendar is a fictional opening label and does not advance from the causal counter. There is no general job planner, trade, crop, injury, death, succession, supernatural, planetary or legal-dispute resolver. Freeform remains unresolved intent. Unknown or missing dependent model data blocks its action rather than receiving a universal default. Wider T01–T37 qualification, historical curation and numerical calibration remain open.

Runtime checks in `test_settlement.py` exercise the bounded contracts, including accounting, competing frontiers, coarse/fine equivalence, pause/resume, revocation, delegation and migration. Host, interface and extraction evidence is recorded separately for the final integrated increment.
