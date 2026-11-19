/* SIRE 2.0 Deck Trainer — user-provided OCIMF Question Library v1.0 (Jan 2022).
   Derived preparation notes only. Never a declaration of inspection compliance. */
import {SIRE_P1A} from './sire_p1a.js';
import {SIRE_P1B} from './sire_p1b.js';
import {SIRE_P1C} from './sire_p1c.js';
import {SIRE_P1D} from './sire_p1d.js';
import {SIRE_P1E} from './sire_p1e.js';
import {SIRE_P2A} from './sire_p2a.js';
import {SIRE_P2B} from './sire_p2b.js';
import {SIRE_P2C} from './sire_p2c.js';
import {SIRE_P2D} from './sire_p2d.js';

const COLLECTION=[...SIRE_P1A,...SIRE_P1B,...SIRE_P1C,...SIRE_P1D,...SIRE_P1E,...SIRE_P2A,...SIRE_P2B,...SIRE_P2C,...SIRE_P2D];
const BANK=[...new Map(COLLECTION.map(q=>[q[0],q])).values()];
const ROOT=document.getElementById('sireDeckTrainer');
const KEY='coSireDeckStudyV1';
const SOURCE='https://www.ocimf.org/programmes/sire-2-0/';
const CAT={cargo:'Ładunek / balast',navigation:'Nawigacja',safety:'Bezpieczeństwo',mooring:'Cumowanie / kotwice',general:'Dokumentacja / załoga',pollution:'MARPOL',security:'ISPS',photos:'Stan techniczny / fotografie',ice:'Żegluga w lodzie'};
const CH={2:'Dokumentacja i SMS',3:'Załoga i szkolenia',4:'Nawigacja i łączność',5:'Bezpieczeństwo',6:'Zapobieganie zanieczyszczeniom',7:'ISPS',8:'Cargo i balast',9:'Mooring i anchoring',11:'Przegląd fotograficzny',12:'Operacje zimowe'};
const CO_HINT={
 cargo:'Pokaż rzeczywisty plan ładunkowy, właściwe zatwierdzone procedury SMS, dokumenty ładunku, zapisy operacji oraz stan instalacji. Dobierz dokumenty do danego rodzaju ładunku i typu statku.',
 navigation:'Wyjaśnij zasadę działania i ograniczenia wyposażenia mostka. Pokaż aktualne procedury nawigacyjne, zapisy testów, passage plan i rzeczywiste demonstracje, jeśli są bezpieczne.',
 safety:'Pokaż analizę ryzyka, PTW/LOTO, szkolenia, dokumenty przeglądów, zapisy ćwiczeń i wyposażenie w miejscu użycia. Sprawdź zgodność z zatwierdzonym SMS.',
 mooring:'Wyjaśnij dobór lin i konfigurację układu cumowniczego, zagrożenia snap-back oraz zasady kontroli wciągarek, hamulców, kotwic i wyposażenia. Pokaż zapisy, jeśli dotyczą danego pytania.',
 general:'Zidentyfikuj właściciela procedury, pokaż aktualne dokumenty i rejestry oraz sposób wykrywania i zamykania niezgodności.',
 pollution:'Sprawdź zapisy wymagane w odpowiednim załączniku MARPOL, zatwierdzone instrukcje, status zbiorników, urządzenia i dokumenty przekazania pozostałości.',
 security:'Sprawdź procedury i familiarisation SSP/ISPS, przy zachowaniu poufności dokumentów i ograniczeń dostępu.',
 photos:'Przygotuj wyłącznie prawdziwe, aktualne fotografie. Porównaj zdjęcia z rzeczywistym stanem pokładu i dokumentacją napraw; nie retuszuj ani nie ukrywaj usterek.',
 ice:'Sprawdź aktualne wymagania rejonu, prognozę lodową, ograniczenia statku, procedury zimowe i familiarisation.'
};
const $=id=>document.getElementById(id);
const make=(tag,cl,content)=>{const e=document.createElement(tag);if(cl)e.className=cl;if(content!==undefined)e.textContent=String(content);return e;};
const section=(label,value)=>{const d=make('div','sire-detail-row');d.append(make('h4','',label),make('p','',value));return d;};
const today=()=>{const d=new Date();return new Date(d.getTime()-d.getTimezoneOffset()*60000).toISOString().slice(0,10);};
function initial(){return {schema:1,reviews:{},vessel:'chemical',chapter:'all',search:'',onlyDue:false};}
function safeRead(v){const out=initial();if(!v||typeof v!=='object')return out;for(const f of ['vessel','chapter','search'])if(typeof v[f]==='string')out[f]=v[f].slice(0,140);out.onlyDue=!!v.onlyDue;
 const valid=new Set(BANK.map(q=>q[0]));if(v.reviews&&typeof v.reviews==='object')for(const [k,val] of Object.entries(v.reviews)){if(!valid.has(k)||!val||typeof val!=='object')continue;
  const rating=['again','soon','confident'].includes(val.rating)?val.rating:'soon';
  const due=/^\d{4}-\d{2}-\d{2}$/.test(val.due||'')?val.due:today();
  out.reviews[k]={rating,due,streak:Math.min(20,Math.max(0,Number(val.streak)||0)),last:String(val.last||'').slice(0,10)};
 }return out;}
let study=initial();try{study=safeRead(JSON.parse(localStorage.getItem(KEY)||'null'));}catch{}
const persist=()=>{try{localStorage.setItem(KEY,JSON.stringify(study));}catch{showMessage('Brak zapisu danych: sprawdź miejsce w przeglądarce. Wykonaj eksport kopii.',true);}};
function showMessage(s,warning=false){const el=$('sireMessage');if(el){el.textContent=s;el.classList.toggle('sire-warning',warning);}}
const vesselMatch=q=>study.vessel==='both'||q[3]==='both'||q[3]===study.vessel;
const countDue=q=>!study.reviews[q[0]]||study.reviews[q[0]].due<=today();
const filtered=()=>BANK.filter(q=>vesselMatch(q)&&(study.chapter==='all'||q[0].split('.')[0]===study.chapter)&&(study.onlyDue?countDue(q):true)&&(!study.search||[q[0],q[1],q[2],q[4],...(q[9]||[])].join(' ').toLowerCase().includes(study.search.toLowerCase())));
const priority=q=>({cargo:0,safety:1,mooring:2,pollution:3,navigation:4,general:5,security:6,ice:7,photos:8}[q[4]]??9);
let chosen=null,revealed=false,listLimit=30;
function choose(id){chosen=String(id);revealed=false;render();}
function mark(value){const q=BANK.find(x=>x[0]===chosen);if(!q)return;
 const prev=study.reviews[chosen],streak=value==='confident'?Math.min(20,(prev?.streak||0)+1):0;
 const days=value==='again'?0:value==='soon'?2:streak===1?7:streak===2?14:streak===3?30:60;
 const d=new Date();d.setDate(d.getDate()+days);study.reviews[chosen]={rating:value,streak,last:today(),due:new Date(d.getTime()-d.getTimezoneOffset()*60000).toISOString().slice(0,10)};
 persist();chosen=null;revealed=false;render();}
function makeBtn(label,fn,variant=''){const b=make('button','sire-btn '+variant,label);b.type='button';b.addEventListener('click',fn);return b;}
function render(){
 if(!ROOT)return;
 const all=filtered().sort((a,b)=>(Number(countDue(b))-Number(countDue(a)))||(priority(a)-priority(b))||a[0].localeCompare(b[0],undefined,{numeric:true}));
 const completed=BANK.filter(q=>study.reviews[q[0]]).length,due=BANK.filter(q=>vesselMatch(q)&&countDue(q)).length;
 $('sireStats').textContent=BANK.length+' pytań w bazie · '+all.length+' spełnia filtry · '+completed+' przećwiczonych · '+due+' do powtórki';
 const list=$('sireList');list.replaceChildren();
 for(const q of all.slice(0,listLimit)){const row=make('button','sire-question-row'+(q[0]===chosen?' selected':'')+(study.reviews[q[0]]?' reviewed':''));row.type='button';row.append(make('strong','',q[0]+' · '+q[1]),make('span','',CAT[q[4]]||q[4]),make('small','',study.reviews[q[0]]?(countDue(q)?'Powtórka teraz':'Powtórka '+study.reviews[q[0]].due):'Nowe pytanie'));row.addEventListener('click',()=>choose(q[0]));list.append(row);}
 $('sireMore').hidden=all.length<=listLimit;
 if(!all.length)list.append(make('p','sire-empty','Brak pytań dla wybranych filtrów. Zmień dział lub wyszukiwanie.'));
 if(!chosen||!all.some(q=>q[0]===chosen))chosen=all[0]?.[0]||null;
 const panel=$('sireDetail');panel.replaceChildren();const q=BANK.find(x=>x[0]===chosen);
 if(!q){panel.append(make('p','sire-empty','Wybierz pytanie lub wyczyść filtry.'));return;}
 const header=make('div','sire-detail-head');header.append(make('div','sire-ref','SIRE 2.0 · '+q[0]+' · '+(CH[q[0].split('.')[0]]||CAT[q[4]])),make('h3','',q[1]));
 if(/^(Were|Was|Had|Did|Does|Is|Are|Has|Have)\b/i.test(q[2]||''))header.append(make('p','sire-full-question',q[2]));panel.append(header);
 if(q[5])panel.append(section('Cel pytania według biblioteki',q[5]));
 if(!revealed){panel.append(make('p','sire-coaching','Najpierw samodzielnie odpowiedz: co sprawdzi inspektor, co pokażesz na statku i jakie są typowe uchybienia. Następnie porównaj odpowiedź z dokumentem.'),makeBtn('Pokaż analizę i dowody',()=>{revealed=true;render();},'primary'));}
 else {
  panel.append(section('Co może sprawdzić inspektor (skrót z OCIMF)',q[6]||'To pytanie dotyczy porównania realnego stanu ze zdjęciem; biblioteka nie zawiera tu standardowej sekcji działań inspektora.'),section('Przykładowe wymagane dowody z biblioteki',q[7]||'Porównanie oryginalnych fotografii z aktualnym stanem i właściwymi zapisami utrzymania.'),section('Możliwe powody negatywnej obserwacji',q[8]||'Niezgodność zdjęcia z rzeczywistym stanem technicznym. Zweryfikuj szczegóły w bibliotece.'));
  panel.append(section('Praktyczna wskazówka treningowa (opracowanie pomocnicze, nie wymóg OCIMF)',CO_HINT[q[4]]||CO_HINT.general));
  panel.append(section('Źródła wymienione w bibliotece',q[9]?.length?q[9].join(' · '):'Brak wyszczególnionych norm przy tej pozycji; sprawdź tekst oryginalny i aktualne SMS.'));
  const actions=make('div','sire-actions');actions.append(makeBtn('Powtórz dziś',()=>mark('again')),makeBtn('Powtórz za 2 dni',()=>mark('soon')),makeBtn('Znam i potrafię pokazać',()=>mark('confident'),'primary'));panel.append(actions);
 }
 const sources=make('div','sire-references'),a=make('a','', 'OCIMF — źródłowa biblioteka SIRE 2.0 ↗');a.href=SOURCE;a.target='_blank';a.rel='noopener noreferrer';sources.append(a);
 if(q[4]==='cargo'||q[4]==='pollution'){const c=make('a','','IMO — Chemical Pollution / MARPOL Annex II ↗');c.href='https://www.imo.org/en/ourwork/environment/pages/chemicalpollution-default.aspx';c.target='_blank';c.rel='noopener noreferrer';sources.append(c);}
 sources.append(makeBtn('Kopiuj pytanie i instrukcję dla AI',()=>copyPrompt(q)));panel.append(sources);
 const status=study.reviews[q[0]];if(status)panel.append(make('p','sire-review-info','Ostatnia ocena: '+status.rating+' · kolejna powtórka: '+status.due));
}
async function copyPrompt(q){
 const prompt='Jesteś doświadczonym Chief Officerem na chemical/oil tanker i trenerem SIRE 2.0. Analizuj pytanie z OCIMF SIRE 2.0 Question Library Part '+(Number(q[0].split('.')[0])<=7?'1':'2')+', v1.0 January 2022: '+q[0]+' — '+q[1]+'.\n\nOryginalny tekst (jeśli dostępny): '+q[2]+'\nCel: '+q[5]+'\nWskazania dotyczące działań inspektora: '+q[6]+'\nExpected evidence: '+q[7]+'\nPotential negative observations: '+q[8]+'\nŹródła wymienione w bibliotece: '+(q[9]||[]).join(', ')+'\n\nPrzygotuj profesjonalne opracowanie po polsku z angielską terminologią: (1) co inspektor sprawdza, (2) teoria i praktyka na chemikaliowcu, (3) przygotowanie i demonstracja, (4) wymagane dokumenty i dowody, (5) częste błędy, (6) przykładowe pytania uzupełniające dla CO/OOW i AB, (7) źródła urzędowe i aktualność na dzień odpowiedzi. Zweryfikuj dokładny przepis, wersję i zastosowanie do statku. Wyraźnie oddziel treść OCIMF 2022 od obecnie obowiązujących wymagań. Nie wymyślaj wyników kontroli, parametrów ani zapisów statkowych. Wszystko weryfikuj z SMS, zatwierdzonymi instrukcjami, IBC, P&A i SDS.';
 try{await navigator.clipboard.writeText(prompt);showMessage('Skopiowano. Wklej do ChatGPT lub Gemini, aby rozwinąć zagadnienie.');}
 catch{const t=make('textarea','sire-prompt-text',prompt);$('sireDetail').append(t);t.select();showMessage('Skopiowanie zablokowane: zaznacz i skopiuj tekst z pola.',true);}
}
function wire(){
 if(!ROOT)return;
 for(const [id,handler] of [['sireVessel',v=>study.vessel=v],['sireChapter',v=>study.chapter=v],['sireSearch',v=>study.search=v.trim().slice(0,140)]])$(id).addEventListener(id==='sireSearch'?'input':'change',e=>{handler(e.target.value);listLimit=30;chosen=null;persist();render();});
 $('sireVessel').value=study.vessel;$('sireChapter').value=study.chapter;$('sireSearch').value=study.search;
 $('sireDueOnly').checked=study.onlyDue;$('sireDueOnly').addEventListener('change',e=>{study.onlyDue=e.target.checked;chosen=null;persist();render();});
 $('sireMore').addEventListener('click',()=>{listLimit+=40;render();});
 $('sireNext').addEventListener('click',()=>{const due=filtered().filter(countDue);const arr=due.length?due:filtered();let next=arr.find(q=>q[0]!==chosen)||arr[0];if(next)choose(next[0]);});
 $('sireExport').addEventListener('click',()=>{const b=new Blob([JSON.stringify({format:'co-sire-deck-training',exported:new Date().toISOString(),study},null,2)],{type:'application/json'}),url=URL.createObjectURL(b),a=make('a');a.href=url;a.download='co_sire_deck_training_backup.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);});
 $('sireClear').addEventListener('click',()=>{study.search='';study.chapter='all';study.onlyDue=false;$('sireSearch').value='';$('sireChapter').value='all';$('sireDueOnly').checked=false;chosen=null;persist();render();});
 window.SIRE_DECK_BACKUP=()=>JSON.parse(JSON.stringify(study));
 window.SIRE_DECK_IMPORT=raw=>{if(!raw)return;study=safeRead(raw);persist();render();};
 render();
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',wire,{once:true});else wire();
