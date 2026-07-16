import html, pathlib
F = pathlib.Path('/tmp/site/files')
def block(name):
    return html.escape(F.joinpath(name).read_text().rstrip())

CSS = """
:root{
  --teal:#13B5A2; --teal-light:#DCFAF5; --teal-dark:#12917E;
  --navy:#132539; --navy-light:#2A3F54; --navy-mute:rgba(19,37,57,0.55);
  --cream:#F9F8F5; --cream-deep:#F2EFE8; --gold:#D4A338;
  --line:rgba(19,37,57,0.08);
  --serif:"Iowan Old Style","Charter","Cochin",Georgia,"Times New Roman",serif;
  --sans:-apple-system,BlinkMacSystemFont,"SF Pro Text","Inter",system-ui,sans-serif;
  --mono:"SF Mono",ui-monospace,"Menlo","JetBrains Mono",monospace;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--cream);color:var(--navy);font-family:var(--sans);line-height:1.6;-webkit-font-smoothing:antialiased}
.wrap{max-width:760px;margin:0 auto;padding:32px 24px 80px}
a{color:var(--teal-dark)}
.eyebrow{font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--navy-mute)}
.brand{display:flex;align-items:center;gap:10px;margin-bottom:28px}
.logo{width:22px;height:22px;background:var(--teal);border-radius:5px;position:relative;flex:0 0 22px}
.logo::after{content:"";position:absolute;inset:6px;background:var(--cream);border-radius:2px}
.brand .eyebrow{font-weight:600;letter-spacing:.16em}
.crumb{margin-bottom:18px}
.pill{display:inline-block;font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:#fff;background:var(--teal);padding:5px 11px;border-radius:999px}
h1{font-family:var(--serif);font-size:44px;line-height:1.06;font-weight:700;margin:16px 0 12px;letter-spacing:-.01em}
.lede{font-size:18px;color:var(--navy-light);max-width:60ch}
.meta{margin-top:14px}
section{margin-top:48px}
.s-label{margin-bottom:6px}
h2{font-family:var(--serif);font-size:27px;font-weight:700;line-height:1.18;margin-bottom:16px;letter-spacing:-.01em}
h3{font-family:var(--serif);font-size:19px;font-weight:700;margin:0 0 8px}
p{margin-bottom:14px;color:#23364a}
ul{margin:0 0 14px 18px;color:#23364a}
li{margin-bottom:5px}
.take{font-weight:700;color:var(--navy);margin:16px 0}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:20px 22px;margin-bottom:12px}
.card.accent{border-left:3px solid var(--teal)}
.callout{font-family:var(--serif);font-size:21px;line-height:1.4;color:var(--navy);background:var(--teal-light);border:1px solid rgba(19,181,162,.22);border-radius:12px;padding:20px 22px;margin:16px 0}
.outcomes{background:#fff;border:1px solid var(--line);border-left:3px solid var(--teal);border-radius:12px;padding:18px 22px;margin:20px 0 0}
.outcomes ul{margin:8px 0 0 18px}
.outcomes li{font-size:15px;color:#23364a}
.part{margin-top:56px;padding-top:14px;border-top:2px solid var(--teal)}
.part .eyebrow{color:var(--teal-dark);font-weight:600}
table{width:100%;border-collapse:separate;border-spacing:0;background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;margin:16px 0;font-size:14px}
th{font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--navy-mute);background:var(--cream-deep);text-align:left;padding:10px 14px;font-weight:600}
td{padding:11px 14px;border-top:1px solid var(--line);color:#23364a;vertical-align:top}
.rung{background:#fff;border:1px solid var(--line);border-left:3px solid var(--teal);border-radius:12px;padding:20px 22px;margin-bottom:12px}
.rung .n{font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--teal-dark);font-weight:600;display:block;margin-bottom:4px}
.rung h3{margin-bottom:10px}
.tradeoff{font-size:14px;margin-top:12px;padding-top:12px;border-top:1px solid var(--line)}
.tradeoff div{margin-bottom:4px;color:#23364a}
.tradeoff b{font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--navy-mute);font-weight:600}
.fileblock{background:#fff;border:1px solid var(--line);border-radius:12px;padding:0;margin:14px 0;overflow:hidden}
.fileblock pre{font-family:var(--mono);font-size:12px;line-height:1.55;color:var(--navy);background:var(--teal-light);padding:16px 18px;margin:0;overflow-x:auto;white-space:pre;border-bottom:1px solid rgba(19,181,162,.22)}
.dl{display:flex;gap:8px;flex-wrap:wrap;padding:12px 14px;background:#fff}
.dl a{display:inline-block;font-family:var(--mono);font-size:11px;letter-spacing:.06em;color:#fff;background:var(--navy);padding:8px 13px;border-radius:7px;text-decoration:none}
.dl a:hover{background:var(--navy-light)}
.dl a.alt{background:#fff;color:var(--navy);border:1px solid var(--line)}
.dl a.alt:hover{background:var(--cream-deep)}
details{background:#fff;border:1px solid var(--line);border-radius:12px;margin-bottom:12px;overflow:hidden}
details summary{cursor:pointer;list-style:none;padding:16px 20px;display:flex;justify-content:space-between;align-items:center;gap:14px}
details summary::-webkit-details-marker{display:none}
details .s-title{font-family:var(--serif);font-size:19px;font-weight:700;color:var(--navy)}
details .s-sub{font-size:13.5px;color:var(--navy-mute);margin-top:2px}
details .chev{font-family:var(--serif);font-size:20px;color:var(--teal);transition:transform .2s ease;line-height:1;flex:0 0 auto}
details[open] .chev{transform:rotate(90deg)}
details .body{padding:2px 20px 20px}
details.open-tier{border-left:3px solid var(--teal)}
.step{background:var(--cream-deep);border-radius:10px;padding:14px 16px;margin-bottom:10px}
.step .n{font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--teal-dark);font-weight:600}
.step ul{margin:6px 0 0 18px}
.step li{font-size:14.5px}
.pitfall{margin-bottom:18px}
.pitfall h3{font-size:17px;margin-bottom:4px}
.pitfall .do{color:var(--navy-mute);font-size:14.5px}
.example{background:#fff;border:1px solid var(--line);border-left:3px solid var(--teal);border-radius:12px;padding:20px 22px;margin:16px 0}
.example p{font-size:15px}
.example p:last-child{margin-bottom:0}
.bridge{background:#fff;border:1px solid var(--line);border-left:3px solid var(--gold);border-radius:12px;padding:22px 24px;margin-top:20px}
.bridge a{display:inline-block;margin-top:10px;font-family:var(--mono);font-size:12px;letter-spacing:.04em;color:#fff;background:var(--navy);padding:9px 15px;border-radius:7px;text-decoration:none}
.bridge a:hover{background:var(--navy-light)}
footer{margin-top:64px;padding-top:20px;border-top:1px solid var(--line);font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--navy-mute)}
@media(max-width:620px){.wrap{padding:24px 18px 64px}h1{font-size:33px}table{font-size:13px}th,td{padding:9px 10px}}
"""

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#F9F8F5">
<title>Conversation Continuity | CHIEF AI Accelerator</title>
<meta name="description" content="Continue your work across a new thread, without repeating yourself. Build the status doc and the skills that keep it current.">
<meta property="og:title" content="Conversation Continuity | CHIEF AI Accelerator">
<meta property="og:description" content="Re-explaining your own work is the most expensive habit you have. This kills it.">
<meta property="og:type" content="article">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">

  <div class="brand">
    <span class="logo"></span>
    <span class="eyebrow">Michael Gardon · CHIEF AI Accelerator</span>
  </div>

  <div class="crumb eyebrow">Accelerator / Curriculum / 2.1 Conversation Continuity</div>
  <span class="pill">Phase 2 · Collaborate</span>

  <h1>Continue your work across a new thread, without repeating yourself</h1>
  <p class="lede">Re-explaining your own work is the most expensive habit you have. This kills it.</p>

  <div class="outcomes">
    <div class="eyebrow">What you'll walk out with</div>
    <ul>
      <li>Carry a project across as many threads as it takes.</li>
      <li>Pick the mode that fits how you already work: manual, connector, or Cowork.</li>
      <li>Build your first skill, so the whole habit runs on one word.</li>
    </ul>
  </div>

  <div class="meta eyebrow">~6 min read · then ~15 min to build it</div>

  <section>
    <div class="s-label eyebrow">Callback</div>
    <h2>The problem</h2>
    <p class="take">You already know a long thread atrophies. But your inclination is to pick up working in the same thread. Here's the habit that works.</p>
    <ul>
      <li>In <b>1.6</b> you learned a long thread degrades. It has a size limit. It weighs recent text more.</li>
      <li>You learned the signs, and when to start fresh instead of pushing.</li>
      <li>And you learned the checkpoint: ask for a handoff before you go, paste it into the next thread.</li>
    </ul>
    <div class="callout">The checkpoint works. It also depends on you remembering to do it, and doing it well, every single time. That's the part that breaks.</div>
    <p class="eyebrow">Need a refresh? → 1.6 Conversation Architecture</p>
    <ul>
      <li>This page gives the handoff a permanent place to live.</li>
      <li>Then it makes one word do the work.</li>
    </ul>
  </section>

  <div class="part"><div class="eyebrow">Part A · The doc</div></div>

  <section>
    <div class="s-label eyebrow">The frame</div>
    <h2>Make your Chief document status</h2>
    <p class="take">Good project documentation means anyone can pick up the work tomorrow. Including someone who wasn't there.</p>
    <ul>
      <li>Back to your new hire from <b>0.1</b>. Brilliant. Knows nothing about you.</li>
      <li>Forget what they know for a second. Look at how a good one <i>operates</i>.</li>
      <li>They keep notes, and organize them into one doc they keep current.</li>
      <li>Decisions get written down the day they're made.</li>
      <li>They never reconstruct where things stand. They already know.</li>
      <li>Somebody out sick? Somebody new on the team? They read the doc and start.</li>
      <li>Nobody has to go hunt down the person who remembers.</li>
    </ul>
    <div class="callout">The test of good project documentation: a stranger can pick up the work without asking you a single question.</div>
    <h3>When you work with AI</h3>
    <ul>
      <li>Every new thread is a bunch of notes not connected to a workstream.</li>
      <li>It wasn't there Tuesday. It has no idea what you decided.</li>
      <li>You've been treating that as a memory problem. It isn't.</li>
      <li>It's a project management problem, and every well-run team already solved it.</li>
    </ul>
    <h3>The one difference</h3>
    <ul>
      <li>A human project manager updates the doc without being told.</li>
      <li>Your Chief won't. Not unless you say so.</li>
      <li>That's the gap. That's all this page closes.</li>
    </ul>
  </section>

  <section>
    <div class="s-label eyebrow">The build</div>
    <h2>How to do this</h2>
    <p class="take">The thread is where the work happens. It is not where the work lives.</p>
    <ul>
      <li>So keep the doc a project manager would keep.</li>
      <li>Not a transcript. Almost none of it. The transcript is mostly noise.</li>
      <li>Keep only what <i>you</i> need to pick up the work.</li>
    </ul>

    <div class="card accent">
      <h3>The status doc</h3>
      <ul>
        <li>What's decided, what's open, what changed, what's next.</li>
        <li>It's what they'd bring to a check-in.</li>
        <li>Rewritten constantly. Stays under a page.</li>
        <li>It replaces scrolling up.</li>
      </ul>
    </div>

    <div class="callout">Status is not a record of what happened. It's a picture of where you are right now, and what's next.</div>

    <h3>The template</h3>
    <p>Notice the first paragraph. <b>The doc tells Chief what to do with it.</b> That's not decoration. A doc that carries its own instructions works even before you build anything.</p>

    <div class="fileblock">
      <pre>{block('status-template.md')}</pre>
      <div class="dl"><a href="/files/status-template.md" download>↓ Download status-template.md</a></div>
    </div>

    <table>
      <thead><tr><th>Section</th><th>What it does for Chief</th><th>What it does for you</th></tr></thead>
      <tbody>
        <tr><td><b>The basics</b></td><td>Frames every answer it gives</td><td>Names which project this is</td></tr>
        <tr><td><b>Status now</b></td><td>Stops it solving a solved problem</td><td>Rebuilds your context in ten seconds</td></tr>
        <tr><td><b>Decisions made</b></td><td>Stops it reopening settled calls</td><td>Stops you re-deciding at 11pm</td></tr>
        <tr><td><b>Ruled out</b></td><td>Stops it pitching the dead option</td><td>Stops the hour-long re-litigation</td></tr>
        <tr><td><b>Open questions</b></td><td>Tells it what to push on</td><td>Tells you what's actually blocked</td></tr>
        <tr><td><b>Next actions</b></td><td>Gives it a starting instruction</td><td>Removes the "where was I" tax</td></tr>
      </tbody>
    </table>

    <ul>
      <li><b>"Status now" is a paragraph, not bullets.</b> Three bullets can't brief someone who wasn't there. Write it like you're catching up a colleague in the hallway.</li>
      <li><b>"Ruled out" is the one people delete.</b> It looks like history. It's the opposite. It's the only section that prevents a conversation you've already had.</li>
    </ul>

    <h3>Setup</h3>
    <ul>
      <li>Ask Chief to create a status doc from your thread, using the template.</li>
      <li>Tell it what format: Google Doc, Word, Notes app, whatever you already use.</li>
      <li>Make sure the status doc gets into your Chief Vault.</li>
      <li>New thread? Paste it in at the top. The new thread walks in briefed.</li>
      <li>You do not need a Project for this. You need a doc and a habit.</li>
    </ul>

    <p class="take">Now you can start any thread from where you left off.</p>

    <div class="card">
      <h3>Pitfall: the status doc that lies</h3>
      <p>A status doc nobody updates is worse than none. You'll trust it.</p>
      <p class="do"><b>What to do:</b> That's why wrap exists. The habit is the system. The doc is just where it writes.</p>
    </div>
  </section>

  <section>
    <div class="s-label eyebrow">The progression</div>
    <h2>Keeping status current</h2>
    <p class="take">Three ways to close the loop. They differ in how much of it your hands have to do.</p>
    <ul>
      <li>The doc only works if it's true.</li>
      <li>So somebody has to update it before you stop.</li>
      <li>Right now that somebody is you. It doesn't have to stay that way.</li>
      <li>Three rungs. Same instruction every time. Less of your hands at each one.</li>
    </ul>

    <div class="rung">
      <span class="n">1 · Beginner</span>
      <h3>Manual: you paste it back</h3>
      <p><b>The command:</b> <i>"Update the status doc before we stop."</i></p>
      <ul>
        <li>That's the whole thing. Six words.</li>
        <li>The doc's own header tells Chief what to do next. You just pull the trigger.</li>
        <li>Chief rewrites it and hands you the text.</li>
        <li>You paste it into your doc. Ten seconds.</li>
      </ul>
      <div class="tradeoff">
        <div><b>Needs:</b> nothing. No connector. No setup. Works today.</div>
        <div><b>Costs:</b> you paste it in at the start, you paste it out at the end.</div>
        <div><b>The catch:</b> it only happens if you remember. That's the whole risk.</div>
      </div>
    </div>

    <div class="rung">
      <span class="n">2 · Intermediate</span>
      <h3>Versioned in your Chief Vault, through a connector</h3>
      <ul>
        <li>Connect Google Drive or OneDrive. Point Chief at your Chief Vault.</li>
        <li>Now it reads the status doc itself. No paste-in.</li>
        <li>At the end, it writes the update back as a new file, dated.</li>
      </ul>
      <p><b>Tradeoffs</b></p>
      <ul>
        <li>A connector doesn't edit your doc inline. It <b>can't</b>.</li>
        <li>It can create new files. It cannot change one that already exists.</li>
        <li><i>(Tested against Google Drive, July 2026. Same behavior on OneDrive.)</i></li>
        <li>So every update lands as a new dated doc, sitting next to the old one.</li>
      </ul>
      <p><b>Which means:</b></p>
      <ul>
        <li><b>Accumulated backlog.</b> You'll have a stack of <span style="font-family:var(--mono);font-size:12px">STATUS &ndash; [project] &ndash; 2026-07-16</span> files. Not a problem, but you'll have to clear them out yourself at some point. Connectors can't delete.</li>
        <li><b>Chief has to always read the most recent.</b> You have to tell it, in thread, to pull the latest version. <i>Until you build the skill. Then it's handled.</i></li>
      </ul>
      <div class="callout">A stack of dated status docs isn't a mess. One undated doc you can't trust is.</div>
      <div class="tradeoff">
        <div><b>Needs:</b> a connector, pointed at your Chief Vault.</div>
        <div><b>Costs:</b> occasional cleanup.</div>
        <div><b>You get back:</b> both pastes. Gone.</div>
      </div>
    </div>

    <div class="rung">
      <span class="n">3 · Pro</span>
      <h3>Automatic, via Cowork</h3>
      <ul>
        <li>Your Chief Vault isn't reached through an API here. It's a folder, on your machine.</li>
        <li>Cowork works in that folder directly.</li>
        <li>It reads the doc. It rewrites the doc. <b>Same file.</b></li>
        <li>No paste. No versions. No cleanup. No stack to sort through.</li>
      </ul>
      <div class="callout">Every other rung ends with your hands. This is the one where the loop closes without you.</div>
      <div class="tradeoff">
        <div><b>Needs:</b> Cowork, with access to your Chief Vault folder. You can keep that folder in the cloud. Cowork works on a synced copy on your machine.</div>
        <div><b>Costs:</b> threads aren't reachable from the web or mobile right now. <a href="/chat-vs-cowork/">Chat vs. Cowork →</a></div>
        <div><b>You gain:</b> documentation done for you, on command. Chief creates, files and organizes all of it.</div>
      </div>
    </div>

    <table>
      <thead><tr><th></th><th>Reads your doc</th><th>Updates your doc</th><th>Your hands</th></tr></thead>
      <tbody>
        <tr><td><b>Beginner</b></td><td>You paste it in</td><td>Hands you text</td><td>Paste in, paste out</td></tr>
        <tr><td><b>Intermediate</b></td><td>Itself</td><td>New dated doc</td><td>Cleanup, sometimes</td></tr>
        <tr><td><b>Pro</b></td><td>Itself</td><td>Same file, in place</td><td>None</td></tr>
      </tbody>
    </table>

    <p class="take">Start at Beginner today. You can climb whenever you want. The doc doesn't change.</p>
  </section>

  <section>
    <div class="s-label eyebrow">The move</div>
    <h2>Turn the command into a skill</h2>
    <p class="take">You keep typing the same instruction. Write it down once, and one word runs it.</p>
    <p><b>Look at what you're actually doing:</b></p>
    <ul>
      <li>Every session ends the same way. You type <i>"update the status doc before we stop."</i></li>
      <li>On Intermediate you type more: read the most recent one, save the new one dated.</li>
      <li>Same words. Every session. Forever.</li>
      <li>Anything you type that often is something you should have written down.</li>
    </ul>
    <p><b>That's a skill:</b></p>
    <ul>
      <li>A skill is written-down instructions for a task you repeat.</li>
      <li>You write it once. After that, one word runs the whole thing.</li>
      <li>The word we'll use is <b>wrap</b>.</li>
      <li>Type it, and everything you've been typing by hand happens.</li>
    </ul>

    <h3>Why not just say "summarize this"?</h3>
    <ul>
      <li>Because the instruction has to be precise, and you won't be precise at 6pm on a Thursday.</li>
      <li>Most people type "summarize this thread" and paste the result into the next one.</li>
      <li>What comes back is a recap of the conversation. What got discussed.</li>
      <li>That's a transcript with fewer words. It's the noise, compressed.</li>
    </ul>

    <div class="example">
      <p>Picture the status update from a project manager who doesn't get it.</p>
      <p><i>"Today we discussed pricing. We talked through several models and considered the competitive landscape. We also touched on the launch timeline."</i></p>
      <p>You now know nothing you didn't know this morning. What did we land on? What's still open? What do you need from me?</p>
      <p>The good one writes four lines. <i>"Pricing is $2,400, flat. Killed the tiers, too hard to explain. Launch date still open, waiting on legal. Need thirty minutes Thursday."</i></p>
    </div>

    <p><b>What you actually need is shorter, and different:</b></p>
    <ul>
      <li>What did we <b>decide</b>? Not what did we discuss.</li>
      <li>What's still <b>open</b>?</li>
      <li>What's the <b>next move</b>?</li>
      <li>What did I <b>rule out</b>, and why?</li>
    </ul>
    <p>That last one is the one people lose. It's also the one you'll waste an hour re-litigating.</p>

    <div class="callout">That's not a summary. It's a handoff. It's what you'd tell your chief of staff on the way out the door.</div>

    <p><b>So here's the case for writing it down:</b></p>
    <ul>
      <li>You could type those four questions every session. You won't.</li>
      <li>The good version takes precision. Precision is what you have least of when you're done for the day.</li>
      <li>A skill holds the precision for you.</li>
    </ul>

    <p class="take">A skill is how you stop depending on your own discipline.</p>
  </section>

  <div class="part"><div class="eyebrow">Part B · Build it</div></div>

  <section>
    <div class="s-label eyebrow">The build</div>
    <h2>Build wrap</h2>
    <p class="take">Fifteen minutes. Then you never type the instruction again.</p>
    <p><b>What you're about to have:</b></p>
    <ul>
      <li>You type <b>wrap</b> at the end of a session.</li>
      <li>It pulls out what changed. Decisions, not discussion.</li>
      <li>It rewrites status and delivers it the way your setup allows.</li>
      <li>You skim it, and close the thread. Nothing was in there.</li>
    </ul>

    <p><b>Where the instructions live is the only choice here.</b> Same text every time. It maps to the three rungs above.</p>

    <table>
      <thead><tr><th>Rung</th><th>Where wrap lives</th><th>What wrap does with the doc</th></tr></thead>
      <tbody>
        <tr><td><b>Beginner</b></td><td>Your Project's instructions</td><td>Hands you the text. You paste it back.</td></tr>
        <tr><td><b>Intermediate</b></td><td>Uploaded to your account</td><td>Saves a new dated doc in your Chief Vault.</td></tr>
        <tr><td><b>Pro</b></td><td>A file in your Chief Vault</td><td>Rewrites the file in place.</td></tr>
      </tbody>
    </table>

    <h3>The instructions</h3>
    <div class="fileblock">
      <pre>{block('wrap-SKILL.md')}</pre>
      <div class="dl">
        <a href="/files/wrap.zip" download>↓ Download wrap.zip</a>
        <a class="alt" href="/files/wrap-SKILL.md" download>↓ SKILL.md (raw)</a>
      </div>
    </div>

    <ul>
      <li>Read the <span style="font-family:var(--mono);font-size:12px">description</span> line twice. It's not a label. It's the trigger.</li>
      <li>It's how Chief decides to fire this when you type "wrap."</li>
      <li>So it has to name the words you'll actually say.</li>
    </ul>

    <div class="card accent">
      <h3>The line that solves the version stack</h3>
      <p>Look at <b>Step 1</b>. <i>"Read only the MOST RECENT one. Ignore the older ones."</i></p>
      <p>On Intermediate, that was your job. You had to remember, every session, to tell Chief which doc was real. Forget once and it briefs you off a stale doc without either of you noticing.</p>
      <p>Now it's in the skill. You don't remember it. It does.</p>
      <p class="do"><b>Step 5 does the same thing.</b> It saves the new doc dated, and it knows not to try to edit or delete the old one, because it can't.</p>
    </div>

    <p class="take">Every rule you were carrying is now in the file.</p>

    <h3>The other half: resume</h3>
    <ul>
      <li><b>wrap</b> closes a session. Something has to open one.</li>
      <li>On <b>Beginner</b> that's easy. You paste the doc in. You're the one choosing.</li>
      <li>On <b>Intermediate</b> it's the whole ballgame. You have a stack of dated docs, and Chief has no idea which one is real.</li>
      <li>Above, that was something you'd have to remember. This is you not having to.</li>
    </ul>

    <div class="fileblock">
      <pre>{block('resume-SKILL.md')}</pre>
      <div class="dl">
        <a href="/files/resume.zip" download>↓ Download resume.zip</a>
        <a class="alt" href="/files/resume-SKILL.md" download>↓ SKILL.md (raw)</a>
      </div>
    </div>

    <div class="card accent">
      <h3>Step 4 is the safety net</h3>
      <p><i>"Name the file you read and its date. If it's more than a week old, say so out loud."</i></p>
      <p>This is the line that catches the failure you'd never catch yourself. Chief reads a stale doc, briefs you confidently off it, and you have no reason to doubt it. Making it say the date out loud turns an invisible failure into an obvious one.</p>
    </div>

    <p><b>Two skills, not one:</b></p>
    <ul>
      <li><b>resume</b> opens. <b>wrap</b> closes. Two files, two uploads.</li>
      <li>Anthropic's own guidance: keep skills focused, one workflow each. Focused skills compose better than one that does everything.</li>
      <li>Say <b>resume</b>. Do the work. Say <b>wrap</b>. That's the whole system.</li>
    </ul>

    <div class="callout">Two words now hold the thing you used to hold in your head.</div>

    <h3>Where to put them</h3>

    <details>
      <summary>
        <div><div class="s-title">Beginner: paste them into a Project</div><div class="s-sub">Least setup, if you already have a Project.</div></div>
        <span class="chev">›</span>
      </summary>
      <div class="body">
        <ul>
          <li>Open your Project → Instructions → paste <b>both</b> blocks above. Done.</li>
          <li><b>You get:</b> wrap and resume fire in any thread inside that Project.</li>
          <li><b>It costs:</b> they only live in that Project.</li>
          <li>Build a second Project? Paste them again.</li>
          <li>Change the wording? Change it in both.</li>
          <li>They don't travel.</li>
        </ul>
        <p><b>Use this if</b> you already work in a Project and want the habit running in five minutes. Upgrading later is a copy and a paste. The text is identical.</p>
        <p><i>Don't have a Project? You don't need one. Use Intermediate.</i></p>
      </div>
    </details>

    <details open class="open-tier">
      <summary>
        <div><div class="s-title">Intermediate: upload them as real skills</div><div class="s-sub">The default. Fifteen minutes once. Then they're everywhere, forever.</div></div>
        <span class="chev">›</span>
      </summary>
      <div class="body">
        <ul>
          <li>Uploaded skills live in your account, not in a Project.</li>
          <li>Every thread. Every Project. Every device.</li>
          <li>You trained the habit once. It doesn't leave when you change desks.</li>
          <li>Works on Free, Pro, Max, Team, and Enterprise. <i>(Checked July 2026.)</i></li>
        </ul>

        <div class="step">
          <span class="n">Step 00 · Check this first</span>
          <ul>
            <li>Settings → Capabilities → turn on <b>code execution</b>.</li>
            <li>Skills don't run without it. This is where people get stuck.</li>
            <li>Thirty seconds now saves a confusing ten minutes later.</li>
          </ul>
        </div>

        <div class="step">
          <span class="n">Step 01 · Download both</span>
          <ul>
            <li>Hit <b>↓ Download wrap.zip</b> and <b>↓ Download resume.zip</b> above.</li>
            <li>Both are already packaged. Folder, SKILL.md, correct structure.</li>
            <li>No folder to build. Nothing to zip.</li>
          </ul>
        </div>

        <div class="step">
          <span class="n">Step 02 · Upload them</span>
          <ul>
            <li>Go to <b>Customize → Skills</b>.</li>
            <li>Upload both ZIPs. Toggle both on.</li>
          </ul>
        </div>

        <div class="step">
          <span class="n">Step 03 · Test them before you trust them</span>
          <ul>
            <li>Open a new chat. Paste in a status doc. Type <b>resume</b>. Then type <b>wrap</b>.</li>
            <li>Watch what each one does.</li>
            <li>Nothing fired? It's one of two things. Code execution is off (Step 00), or the <span style="font-family:var(--mono);font-size:12px">description</span> doesn't include the word you typed.</li>
            <li>Fix the description. Re-upload.</li>
          </ul>
        </div>

        <div class="step">
          <span class="n">Step 04 · Use them for real</span>
          <ul>
            <li>Next work session, type <b>wrap</b> at the end.</li>
            <li>Do it once and you'll feel the difference on the way back in.</li>
          </ul>
        </div>

        <p><b>Want to change one first?</b> Download the raw SKILL.md, edit it, then paste it into a new chat and say: <i>"Package this as a ZIP I can upload in Customize &gt; Skills. One folder called wrap at the root, with SKILL.md inside."</i> Worth doing once, just to see that Chief can package its own skills. That's the whole trick behind Phase 3.</p>

        <div class="callout">You just built a skill. That's the whole mechanism. Phase 3 is this, with bigger instructions.</div>
      </div>
    </details>

    <details>
      <summary>
        <div><div class="s-title">Pro: keep them in your Chief Vault</div><div class="s-sub">For when your files and your Chief are in the same place.</div></div>
        <span class="chev">›</span>
      </summary>
      <div class="body">
        <ul>
          <li>In Cowork or Claude Code, a skill is a file in your folder.</li>
          <li>It sits next to the work it's about.</li>
        </ul>
        <p><b>You get:</b></p>
        <ul>
          <li><b>No paste-back.</b> It rewrites your status doc on disk. You never touch it.</li>
          <li>You edit the skill like any file.</li>
          <li>It's version-controlled. See what it looked like in March. Roll back a change that made it worse.</li>
          <li>It lives next to your status doc and your work. Not in a settings menu.</li>
        </ul>
        <p><b>It costs:</b></p>
        <ul>
          <li>You need a folder Chief can reach.</li>
          <li>You need to be comfortable with files.</li>
          <li>Different surface, different tradeoffs.</li>
        </ul>
        <p><b>Use this if</b> you already work out of a real folder. If that sentence meant nothing to you, use Intermediate. You lose nothing. Same file. It moves when you're ready.</p>
        <p><i>Which surface to use when is its own thing. <a href="/chat-vs-cowork/">Chat vs. Cowork →</a></i></p>
      </div>
    </details>
  </section>

  <section>
    <div class="s-label eyebrow">The rhythm</div>
    <h2>What good looks like</h2>
    <p class="take">Two minutes at the end buys you a warm start every time.</p>
    <div class="step"><span class="n">01</span><ul><li><b>Open a new thread. Type resume.</b> It finds the doc, reads the current one, tells you where you are.</li></ul></div>
    <div class="step"><span class="n">02</span><ul><li><b>Do one job.</b> Just the one.</li></ul></div>
    <div class="step"><span class="n">03</span><ul><li><b>Watch for the signs.</b> You know these from 1.6. Don't push through them.</li></ul></div>
    <div class="step"><span class="n">04</span><ul><li><b>Type wrap.</b> Skim what it wrote. Fix what it got wrong. Ten seconds, and it matters more than the whole thread.</li></ul></div>
    <div class="step"><span class="n">05</span><ul><li><b>Close it.</b> Nothing was in there.</li></ul></div>
    <p>Two words. Everything between them is the actual work.</p>

    <div class="card accent">
      <h3>Four things to carry out</h3>
      <ul>
        <li>The thread is where work happens, not where it lives.</li>
        <li>Status is the doc. <b>resume</b> opens it, <b>wrap</b> closes it.</li>
        <li>Decisions, not discussion. A summary of what you talked about is worth nothing.</li>
        <li>A skill is a standing instruction. You just built two. That's the rest of the program.</li>
      </ul>
    </div>
  </section>

  <section>
    <div class="s-label eyebrow">Watch for these</div>
    <h2>Pitfalls</h2>

    <div class="pitfall">
      <h3>The status doc that grows.</h3>
      <ul><li>Six weeks in it's four pages. You've stopped reading it.</li>
      <li>Now you're pasting four pages of stale context into every thread.</li></ul>
      <p class="do"><b>What to do:</b> Status is where you are, not how you got here. If it's settled and it doesn't shape the next move, cut it. Over a page? Cut.</p>
    </div>

    <div class="pitfall">
      <h3>Wrapping only when the thread is dying.</h3>
      <ul><li>You wrap when you feel the wall coming.</li>
      <li>So you only ever capture the messy end.</li></ul>
      <p class="do"><b>What to do:</b> Wrap when the job is done, not when the thread is done. Different moments.</p>
    </div>

    <div class="pitfall">
      <h3>Trusting the wrap.</h3>
      <ul><li>It guessed. Usually well.</li>
      <li>Sometimes it records a decision you never made. Now that's your source of truth.</li></ul>
      <p class="do"><b>What to do:</b> Read it. Ten seconds. You'd read a status update before acting on it. Read this one.</p>
    </div>

    <div class="pitfall">
      <h3>Forgetting to paste it back.</h3>
      <ul><li>You wrapped. You read it. You closed the thread. You never saved it.</li></ul>
      <p class="do"><b>What to do:</b> The wrap isn't done until the doc changed. This is the one step Pro deletes.</p>
    </div>

    <div class="pitfall">
      <h3>The thread that keeps going anyway.</h3>
      <ul><li>You have the system. You're still in a four-day thread. It's right there, and it's warm.</li></ul>
      <p class="do"><b>What to do:</b> Having the system doesn't remove the pull. 1.6 told you the signs. Wrap and close.</p>
    </div>
  </section>

  <div class="bridge">
    <div class="eyebrow">What's next</div>
    <h3>2.2 · Projects &amp; Context</h3>
    <ul>
      <li>You have the habit. Now stop pasting.</li>
      <li>A Project loads status for you, and holds the brief you're tired of repeating.</li>
    </ul>
    <a href="/">Back to the program map →</a>
  </div>

  <footer>Michael Gardon · CHIEF AI Accelerator — 2.1 Conversation Continuity</footer>

</div>
</body>
</html>
"""
pathlib.Path('/tmp/site/continuity/index.html').write_text(HTML)
print("built:", len(HTML), "bytes")
