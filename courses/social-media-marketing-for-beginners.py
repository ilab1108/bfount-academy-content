# Builds courses/social-media-marketing-for-beginners.json (kept as Python for readable multi-line HTML).
import json, os

course = {
  "title": "Social Media Marketing for Beginners",
  "slug": "social-media-marketing-for-beginners",
  "category_id": 3,
  "level": "beginner",
  "icon": "📱",
  "sort_order": 120,
  "summary": "Learn organic social media marketing from scratch: pick the right platforms, set up profiles that convert, plan content pillars, create scroll-stopping posts, turn followers into leads and measure what works.",
  "outcomes": "\n".join([
    "Set a clear business goal for social media and connect it to a simple funnel",
    "Choose one or two platforms that fit your customers and set up profiles that convert",
    "Plan content pillars and a realistic weekly posting calendar",
    "Write hooks, captions and short-video scripts that earn attention",
    "Turn comments, DMs and followers into leads you own",
    "Track the metrics that matter and run a 30-minute monthly review",
  ]),
  "description": "<p>Most small businesses post on social media without a plan, get a few likes and give up. This course shows you a simpler, more reliable way: choose the right platform, post useful content consistently, and give people a clear next step so attention turns into enquiries and sales.</p><p>Every lesson is short and practical, with a real-world example, a checklist and a small assignment. By the end you will have a 30-day social media plan for a real or imaginary business — ready to use for your own brand, a client or a job interview. No ad budget is needed.</p>",
  "project": "Create a 30-day social media plan for a real or imaginary small business: the goal and target customer, one or two chosen platforms and why, an optimised profile (bio, link, call to action), 3–4 content pillars, a 30-day calendar with at least 12 posts, three fully written posts (hook, body, caption, call to action), a plan for turning followers into leads, and the metrics you will review at the end of the month.",
  "status": "published",
  "modules": [
    {"title": "Module 1 · Social media foundations", "lessons": []},
    {"title": "Module 2 · Create, grow and measure", "lessons": []},
    {"title": "Module 3 · Your 30-day social media plan", "lessons": []},
  ],
}

L = []

L.append({"module": 0, "title": "How social media marketing works for a business", "slug": "how-social-media-marketing-works", "minutes": 11, "free_preview": True,
"intro": "Social media marketing is not about going viral. It is about showing up consistently where your customers already spend time, earning their trust, and giving them an easy next step. This lesson gives you the big picture before you post anything.",
"body": """<h2>What social media marketing really is</h2>
<p>Social media marketing means using platforms such as Instagram, Facebook, LinkedIn, TikTok and YouTube to <strong>reach</strong> the right people, <strong>build trust</strong> with useful content and <strong>move them</strong> toward becoming customers. It has two sides:</p>
<table>
<thead><tr><th></th><th>Organic social</th><th>Paid social</th></tr></thead>
<tbody>
<tr><td>What it is</td><td>Posts, videos, comments and messages you publish for free</td><td>Ads you pay to show to a chosen audience</td></tr>
<tr><td>Main cost</td><td>Time and creativity</td><td>Ad spend</td></tr>
<tr><td>Speed</td><td>Builds over weeks and months</td><td>Results in days</td></tr>
<tr><td>Best for</td><td>Trust, community, proof and repeat customers</td><td>Reaching new people at scale</td></tr>
</tbody>
</table>
<p>This course focuses on <strong>organic social</strong>. When you are ready to add ads, the <a href="/academy/courses/meta-ads-mastery/">Meta Ads Mastery</a> course is the next step — and good organic content makes better ads, because you already know what your audience responds to.</p>
<h2>Start with one business goal</h2>
<p>"Get more followers" is not a business goal. Pick one goal that matters to the business for the next 90 days:</p>
<ul>
<li><strong>Enquiries or bookings</strong> — common for local services, coaches and agencies.</li>
<li><strong>Online sales</strong> — common for shops and product brands.</li>
<li><strong>Email sign-ups</strong> — building an audience you own.</li>
<li><strong>Awareness in a new area</strong> — for a new business or new location.</li>
</ul>
<p>Your goal decides what you post, which call to action you use and which numbers you watch.</p>
<h2>The social media funnel</h2>
<ol>
<li><strong>Discover:</strong> someone sees your post in a feed, on a Reels or Shorts tab, in search or because a friend shared it.</li>
<li><strong>Trust:</strong> they visit your profile, see more useful posts and proof (reviews, results, behind the scenes) and decide to follow.</li>
<li><strong>Act:</strong> they click your link, send a message, book, buy or sign up.</li>
<li><strong>Return:</strong> they keep seeing your content, buy again and recommend you.</li>
</ol>
<p>Beginners usually work only on "discover". They post, hope for likes, and never give people a clear way to act. Every good social plan has something for all four stages.</p>
<h2>How the platforms decide who sees your post</h2>
<p>Each platform uses a recommendation system that tries to show people content they are likely to enjoy. The exact signals change often and are not fully public, but across platforms the same habits help:</p>
<ul>
<li>Content people <strong>watch to the end, save, share or comment on</strong> tends to be shown to more people.</li>
<li><strong>Original</strong> content is favoured over reposted material — Instagram, for example, has said it gives priority to original creators over accounts that mainly repost.</li>
<li>Posting consistently gives the platform more chances to learn who your content is for.</li>
</ul>
<p>You cannot control the algorithm, but you can control whether your content is useful, original and clear about who it is for.</p>
<h2>A realistic expectation</h2>
<p>Organic social is a long game. Expect to post consistently for at least two to three months before you can judge what works. That is why choosing a manageable plan — not an ambitious one you abandon — matters so much.</p>""",
"example": "<p>A mobile dog groomer posted cute dog photos every day and gained followers, but bookings did not change. She set one goal — more bookings in her town — added a \"Book a groom\" link and button to her profile, and ended each post with a simple next step such as \"DM 'GROOM' for this week's free slots\". The same effort started turning into booking messages because every post now had a job to do.</p>",
"checklist": "I know the difference between organic and paid social\nI have one business goal for the next 90 days\nI can explain the discover → trust → act → return funnel\nI know which signals usually help a post reach more people\nI am ready to commit to a realistic plan for at least two to three months",
"assignment": "<p>Pick a real or imaginary business. Write its one 90-day social media goal, then one line for each funnel stage: how people will discover you, what will build their trust, what action you want them to take, and how you will bring them back.</p>",
"video_script": "Hook: More followers, same number of bookings — here's what was missing.\nOrganic vs paid social in one table.\nPick one business goal, not 'more followers'.\nThe funnel: discover, trust, act, return.\nWhat helps posts reach more people.\nSet a realistic timeline.\nAssignment: your goal and four-line funnel.",
"quiz": [
  {"q": "Which of these is a business goal rather than a vanity goal?", "opts": ["Reach 10,000 followers", "Get 20 booking enquiries a month", "Get more likes", "Post every day"], "correct": 1, "exp": "Enquiries connect directly to revenue; followers and likes only matter if they lead to action."},
  {"q": "What is the main cost of organic social media?", "opts": ["Ad spend", "Time and creativity", "Platform subscription fees", "Paying influencers"], "correct": 1, "exp": "Organic posting is free to publish, but it takes time and creative effort."},
  {"q": "Which stage do beginners most often forget?", "opts": ["Discover", "Act — giving people a clear next step", "Posting photos", "Using hashtags"], "correct": 1, "exp": "Without a clear call to action and link, attention rarely turns into enquiries or sales."},
]})

L.append({"module": 0, "title": "Choosing your platforms and setting up profiles that convert", "slug": "choosing-platforms-and-profiles", "minutes": 12, "free_preview": False,
"intro": "You do not need to be everywhere. This lesson helps you choose one or two platforms where your customers already spend time and set up a business profile that turns visitors into followers and followers into enquiries.",
"body": """<h2>Choose one or two platforms</h2>
<p>Being average on five platforms is worse than being good on one. Start with the platform where your customers already spend time and where your type of content fits.</p>
<table>
<thead><tr><th>Platform</th><th>Strong fit</th><th>Content that works</th></tr></thead>
<tbody>
<tr><td>Instagram</td><td>Local businesses, visual products, food, fitness, beauty, lifestyle</td><td>Reels, carousels, Stories</td></tr>
<tr><td>Facebook</td><td>Local communities, groups, events, many older audiences</td><td>Posts, groups, video, events</td></tr>
<tr><td>LinkedIn</td><td>B2B, professional services, recruiting, consultants</td><td>Text posts, documents, short video</td></tr>
<tr><td>TikTok</td><td>Reaching new audiences, products with a story, younger buyers</td><td>Short, native-style video</td></tr>
<tr><td>YouTube (and Shorts)</td><td>How-to and research-heavy purchases</td><td>Tutorials, reviews, Shorts</td></tr>
<tr><td>Pinterest</td><td>Home, wedding, recipes, fashion, DIY — planned purchases</td><td>Pins linking to your site</td></tr>
</tbody>
</table>
<p>Three questions decide it: <strong>Where are my customers?</strong> <strong>What content can I make every week?</strong> <strong>Which platform suits how people buy what I sell?</strong> If you are building a personal brand for B2B, see <a href="/academy/courses/linkedin-personal-brand/">LinkedIn Personal Brand</a>.</p>
<h2>Use a business or professional account</h2>
<p>Switch to a business, creator or professional account (or a Page on Facebook and LinkedIn). These are free and give you insights (analytics), contact buttons, scheduling and the option to run ads later. On Meta, connecting your Facebook Page and Instagram account lets you manage both — including posts, messages and insights — from Meta Business Suite.</p>
<h2>The profile checklist</h2>
<p>Your profile is your shop window. New visitors decide in seconds whether to follow, click or leave.</p>
<ol>
<li><strong>Name and handle:</strong> your business name, easy to spell and the same across platforms where possible. On Instagram, the name field is searchable, so you can add a keyword: "Lena's Bakery | Birthday Cakes Austin".</li>
<li><strong>Profile photo:</strong> your logo for a brand, a clear face photo for a personal brand. It must be readable at a tiny size.</li>
<li><strong>Bio in three lines:</strong> who you help, what you offer, why you (proof or difference), then a call to action. Example: "Custom birthday cakes in Austin 🎂 · 500+ five-star reviews · Order 7 days ahead ↓".</li>
<li><strong>Link:</strong> send people to one focused page — a booking page, a lead magnet or a simple link page with three to five options. Add UTM tags so analytics shows the traffic came from your profile.</li>
<li><strong>Contact buttons:</strong> add call, email, book or directions buttons where available.</li>
<li><strong>Highlights, featured or pinned posts:</strong> pin your best introduction, your offer and your reviews so new visitors see proof first.</li>
<li><strong>Consistent branding:</strong> the same colours, fonts and tone across your profile and posts.</li>
</ol>
<h2>Security basics</h2>
<p>Turn on two-factor authentication, use a business email you control, and give team members their own access through the platform's business tools rather than sharing one password. Losing a hacked account can wipe out years of work.</p>
<h2>Claim your name everywhere, focus on one</h2>
<p>It is fine to reserve your handle on other platforms so nobody else takes it. Just do not spread your effort until your main platform is working.</p>""",
"example": "<p>A bookkeeping firm tried Instagram, TikTok and Facebook at once and posted rarely on all three. After checking where their clients — small business owners — actually looked for advice, they focused only on LinkedIn and a Facebook Page linked to their Google Business Profile. They rewrote the bio to \"Bookkeeping for Ohio contractors · Monthly fixed fee · Book a free 15-min call ↓\" and linked to a booking page. With one channel and a clear profile, consultation requests became steady.</p>",
"checklist": "I chose one or two platforms using the three questions\nI use a free business, creator or professional account\nMy name and handle are consistent and searchable\nMy bio says who I help, what I offer, why me and what to do next\nMy link goes to one focused page with UTM tags\nMy best posts, offer and reviews are pinned or highlighted\nTwo-factor authentication is turned on",
"assignment": "<p>Choose your main platform and write one sentence explaining why. Then rewrite your profile: name field, three-line bio with a call to action, the link destination, and the three posts or highlights you will pin.</p>",
"video_script": "Hook: Three platforms, no results — then one platform changed everything.\nPick one or two platforms with three questions.\nSwitch to a business or professional account.\nThe seven-point profile checklist.\nSecurity basics.\nAssignment: rewrite your bio and pick your pinned posts.",
"quiz": [
  {"q": "A consultant sells services to other businesses. Which platform is usually the best place to start?", "opts": ["Pinterest", "LinkedIn", "Snapchat", "Twitch"], "correct": 1, "exp": "LinkedIn is where business decision-makers and professionals spend time."},
  {"q": "What should a good bio end with?", "opts": ["A list of hashtags", "A clear call to action", "Your full address", "A famous quote"], "correct": 1, "exp": "The bio should tell visitors exactly what to do next — book, order, sign up or message."},
  {"q": "Why switch to a business or professional account?", "opts": ["It guarantees more reach", "It unlocks insights, contact buttons and ad tools", "It removes all ads from your feed", "It is required to post photos"], "correct": 1, "exp": "Business accounts are free and give you analytics, contact options and the ability to advertise."},
]})

L.append({"module": 0, "title": "Content pillars, formats and a weekly calendar", "slug": "content-pillars-and-calendar", "minutes": 12, "free_preview": False,
"intro": "\"What should I post?\" is the question that makes most people quit. Content pillars, a small set of formats and a simple weekly calendar answer it once, so posting becomes a routine instead of a daily struggle.",
"body": """<h2>Content pillars: your 3–4 recurring themes</h2>
<p>A content pillar is a theme you post about again and again. Pillars make planning easy and teach your audience what to expect. A simple mix that works for most businesses:</p>
<table>
<thead><tr><th>Pillar type</th><th>Purpose</th><th>Example for a fitness studio</th></tr></thead>
<tbody>
<tr><td>Educate</td><td>Solve a small problem; earns saves and shares</td><td>"3 stretches for desk workers"</td></tr>
<tr><td>Prove</td><td>Show results and reviews; builds trust</td><td>Member stories, before/after progress</td></tr>
<tr><td>Behind the scenes</td><td>Show the people and process; builds connection</td><td>A coach's morning, setting up a class</td></tr>
<tr><td>Offer</td><td>Make a clear invitation; drives action</td><td>"Free first class this week — DM 'TRIAL'"</td></tr>
</tbody>
</table>
<p>A useful rule of thumb: most posts should help, teach or entertain, and a smaller share should sell. If every post is an advert, people stop paying attention. If no post ever sells, nobody knows how to buy.</p>
<h2>Find ideas from real customer questions</h2>
<ul>
<li>List the 20 questions customers ask before they buy. Each one is a post.</li>
<li>Note objections ("Is it too expensive?", "Will it work for me?") and answer them honestly.</li>
<li>Read comments on competitors' posts and reviews for the words customers use.</li>
</ul>
<p>Our <a href="/academy/courses/customer-research-positioning/">Customer Research &amp; Positioning</a> course shows how to collect these questions in a structured way.</p>
<h2>Pick two or three formats you can sustain</h2>
<ul>
<li><strong>Short vertical video</strong> (Reels, TikTok, Shorts): usually the best way to reach new people. Keep it tight and get to the point in the first seconds.</li>
<li><strong>Carousels and documents:</strong> step-by-step tips people save and come back to.</li>
<li><strong>Single image or text post:</strong> quick updates, quotes, announcements; text posts work well on LinkedIn.</li>
<li><strong>Stories:</strong> casual daily updates, polls and questions for people who already follow you.</li>
</ul>
<p>Turn one idea into several formats: a tip becomes a Reel, a carousel and a Story poll. This is called <strong>repurposing</strong>, and it is how small teams keep up.</p>
<h2>Choose a frequency you can keep</h2>
<p>There is no magic number. Consistency matters more than volume: three good posts a week for six months beat daily posts for two weeks followed by silence. For most beginners, two to four feed posts a week plus a few Stories is a realistic start.</p>
<h2>The weekly calendar and batching</h2>
<ol>
<li><strong>Plan (30 minutes):</strong> pick next week's posts from your pillars and question list.</li>
<li><strong>Create (1–2 hours):</strong> film several videos and design posts in one session.</li>
<li><strong>Schedule:</strong> use the platforms' own free schedulers (such as Meta Business Suite for Facebook and Instagram) or a scheduling tool.</li>
<li><strong>Engage (10–15 minutes a day):</strong> reply to comments and messages — this part cannot be scheduled.</li>
</ol>
<p>A shared spreadsheet with columns for date, platform, pillar, format, hook, call to action and status is all the "content calendar" you need.</p>
<h2>Keep a swipe file and an ideas bank</h2>
<p>Whenever you see a post that makes you stop, save it to a private collection and note <em>why</em> it worked — the hook, the format, the story. Do not copy it; use the idea as a prompt for your own version. Keep a running list of post ideas on your phone so that planning day starts with twenty options, not a blank page.</p>""",
"example": "<p>A family-run Italian restaurant used four pillars: \"from our kitchen\" (behind the scenes), \"pasta tips\" (educate), \"guest of the week\" (prove) and \"this week's special\" (offer). Every Monday the owner filmed four short videos in an hour and scheduled them for the week. Planning stopped being a daily headache, and regulars started asking for the dishes they had seen in the videos.</p>",
"checklist": "I have 3–4 content pillars that cover educate, prove, behind the scenes and offer\nI listed at least 20 customer questions as post ideas\nI chose two or three formats I can make every week\nI picked a posting frequency I can sustain for months\nI have a simple content calendar and a weekly batching session\nI block 10–15 minutes a day to reply to comments and messages",
"assignment": "<p>Write your 3–4 content pillars with one example post each. Then fill in a one-week calendar (date, platform, pillar, format, hook, call to action) for the posting frequency you chose.</p>",
"video_script": "Hook: The restaurant that plans a whole week of posts in one hour.\nContent pillars: educate, prove, behind the scenes, offer.\nIdeas from real customer questions.\nPick formats you can sustain — and repurpose.\nConsistency over volume.\nThe weekly batching routine.\nAssignment: pillars and a one-week calendar.",
"quiz": [
  {"q": "What is a content pillar?", "opts": ["A paid ad format", "A recurring theme you post about", "A type of hashtag", "The first post on your profile"], "correct": 1, "exp": "Pillars are the 3–4 themes that make content easy to plan and recognise."},
  {"q": "What is repurposing?", "opts": ["Deleting old posts", "Turning one idea into several formats", "Buying content from other accounts", "Reposting competitors' videos"], "correct": 1, "exp": "One tip can become a short video, a carousel and a Story — more content for the same thinking."},
  {"q": "Which part of social media cannot be scheduled in advance?", "opts": ["Feed posts", "Replying to comments and messages", "Reels", "Carousels"], "correct": 1, "exp": "Engagement — replying to people — has to happen live, so block a little time for it every day."},
]})

L.append({"module": 1, "title": "Creating posts that stop the scroll: hooks, video and captions", "slug": "creating-scroll-stopping-posts", "minutes": 13, "free_preview": False,
"intro": "People decide in a moment whether to keep watching or scroll past. This lesson gives you simple formulas for hooks, short videos, carousels and captions — plus the rules for honest, original content.",
"body": """<h2>The hook decides everything</h2>
<p>The first line of text or the first seconds of a video must give people a reason to stay. Hook formulas that work across platforms:</p>
<ul>
<li><strong>Call out the viewer:</strong> "If you own a small café, watch this."</li>
<li><strong>Name the mistake:</strong> "Stop washing your car with dish soap."</li>
<li><strong>Promise a result:</strong> "How we cut our client's no-shows in half."</li>
<li><strong>Show the end first:</strong> start with the finished cake, then show how it was made.</li>
<li><strong>Ask a real question:</strong> "Why does your bread come out flat?"</li>
</ul>
<p>Put the hook on screen as text too — many people watch with the sound off. Most platforms can generate captions automatically; check them for mistakes.</p>
<h2>A simple short-video structure</h2>
<ol>
<li><strong>Hook</strong> (first 1–3 seconds): the reason to watch.</li>
<li><strong>Value</strong>: the tip, story or demonstration — one idea only.</li>
<li><strong>Proof or payoff</strong>: the result, the before/after, the punchline.</li>
<li><strong>Next step</strong>: "Save this", "Follow for part 2", "DM 'PRICE' for our menu".</li>
</ol>
<p>You do not need expensive gear. A recent phone, natural light from a window and a quiet room are enough. Film vertically, keep the subject close to the camera and cut out pauses. Shorter is usually better for a first video; only make it longer if every second earns its place.</p>
<h2>Carousels that get saved</h2>
<ul>
<li>Slide 1 is the hook, written like a headline.</li>
<li>One idea per slide, with large readable text.</li>
<li>The last slide gives the next step.</li>
</ul>
<h2>Captions that sell without shouting</h2>
<p>A caption expands on the post and tells people what to do. Use the <strong>problem → insight → next step</strong> pattern: name a problem the reader has, share one useful insight, and finish with a single clear call to action. Write the way your customer talks. For a deeper toolkit, see <a href="/academy/courses/copywriting-that-sells/">Copywriting That Sells</a>.</p>
<p>Hashtags and keywords: platforms increasingly use the words in your caption, on-screen text and spoken audio to understand a post and show it in search. Use a few specific, relevant hashtags and keywords rather than long lists of popular ones.</p>
<h2>Original and honest content</h2>
<ul>
<li><strong>Make it yours.</strong> Platforms say they favour original content and may reduce the reach of accounts that mainly repost others' work. Film your own footage and add your own perspective.</li>
<li><strong>Respect copyright.</strong> Use the platform's licensed music library for business accounts, and do not use other people's photos or videos without permission.</li>
<li><strong>Disclose partnerships.</strong> In the US, the FTC's Endorsement Guides require a clear and conspicuous disclosure when there is a material connection — payment, free products or a family or business relationship. Use plain words such as "Ad" or "Paid partnership" that people will actually notice, not a hashtag buried at the end.</li>
<li><strong>No fake proof.</strong> Never invent reviews or results, and never buy followers or engagement.</li>
</ul>
<h2>Test and learn</h2>
<p>Treat each post as a small experiment. Change one thing at a time — the hook, the format, the length — and note what gets more watch time, saves and shares. Some platforms offer tools for this; Instagram's trial reels, for example, let eligible accounts show a Reel to non-followers first before sharing it with followers.</p>""",
"example": "<p>An auto detailer's videos opened with a slow pan of the shop and got few views. He changed the first second to the dirtiest part of a car with the on-screen text \"This took 4 hours to fix\", then showed the process in quick cuts and ended on the finished result with \"DM 'DETAIL' for a quote\". Viewers stayed to see the reveal, and quote requests started arriving through DMs.</p>",
"checklist": "Every post opens with a clear hook in the first line or first seconds\nVideos have on-screen text and checked captions\nEach video follows hook → value → proof → next step\nCarousel slide 1 is a headline and the last slide is a call to action\nCaptions use problem → insight → next step\nMy content is original, licensed and honest\nPaid partnerships are clearly disclosed",
"assignment": "<p>Write five hooks for your business using five different formulas. Then script one short video (hook, value, proof, next step) and one caption using problem → insight → next step.</p>",
"video_script": "Hook: The detailer who changed one second and started getting quote requests.\nFive hook formulas.\nThe short-video structure: hook, value, proof, next step.\nCarousels people save.\nCaptions: problem, insight, next step.\nOriginal, honest content and FTC disclosure.\nTest one thing at a time.\nAssignment: five hooks and one script.",
"quiz": [
  {"q": "Why should you add on-screen text to the hook of a video?", "opts": ["Platforms require it", "Many people watch with the sound off", "It makes the video longer", "It replaces the caption"], "correct": 1, "exp": "On-screen text makes the hook work for people scrolling with sound off."},
  {"q": "A creator received a free product from your brand and posts about it. What do the FTC's guides expect?", "opts": ["No disclosure, because no money changed hands", "A clear, conspicuous disclosure such as 'Ad' or 'Gifted'", "A hashtag hidden among 30 others", "Disclosure only on YouTube"], "correct": 1, "exp": "A free product is a material connection, so it must be disclosed clearly where people will notice it."},
  {"q": "What is the best way to learn what content works?", "opts": ["Change everything every post", "Change one thing at a time and compare results", "Copy viral videos from other accounts", "Post only once a month"], "correct": 1, "exp": "Changing one variable at a time shows you what actually made the difference."},
]})

L.append({"module": 1, "title": "Engagement, community and turning followers into leads", "slug": "engagement-and-social-leads", "minutes": 12, "free_preview": False,
"intro": "Followers belong to the platform; leads and customers belong to you. This lesson shows how to build real conversations, use comments and DMs to start sales, and move people to your website or email list.",
"body": """<h2>Social media is social</h2>
<p>Posting and leaving is broadcasting. The accounts that grow fastest in trust treat comments and messages as conversations. Make it a daily habit:</p>
<ul>
<li><strong>Reply to every genuine comment</strong>, ideally with a question that keeps the conversation going.</li>
<li><strong>Answer DMs quickly.</strong> A message is often a buying signal — the faster you reply, the more likely you win the customer. Our article on <a href="/academy/speed-to-lead-follow-up/">speed to lead</a> explains why minutes matter.</li>
<li><strong>Engage outward:</strong> leave useful comments on posts by local businesses, partners and people in your industry. It puts your name in front of their audience.</li>
<li><strong>Handle complaints in public, calmly:</strong> acknowledge, apologise if needed, and move the details to a private message. Others are watching how you respond.</li>
</ul>
<h2>Calls to action that start conversations</h2>
<p>Different calls to action suit different goals. Use one per post:</p>
<table>
<thead><tr><th>Goal</th><th>Call to action</th></tr></thead>
<tbody>
<tr><td>Reach</td><td>"Share this with a friend who…" / "Save this for later"</td></tr>
<tr><td>Conversation</td><td>"Comment 'GUIDE' and I'll send it to you"</td></tr>
<tr><td>Leads</td><td>"Get the free checklist — link in bio"</td></tr>
<tr><td>Sales</td><td>"Book this week's slots — link in bio"</td></tr>
</tbody>
</table>
<p>The "comment a keyword" approach works well because it creates engagement and lets you send a link in a private message. If you automate the replies with an approved tool, keep the message helpful and personal, and always let a real person take over when someone asks a question.</p>
<h2>Move followers onto channels you own</h2>
<p>Algorithms change, accounts get hacked, platforms rise and fall. An email list or a customer list keeps your business safe. Offer a <strong>lead magnet</strong> — something quick and useful in exchange for an email:</p>
<ul>
<li>A checklist, template or price guide</li>
<li>A discount or free first session</li>
<li>A short challenge or mini-course</li>
</ul>
<p>Send people to a simple landing page with one form, then follow up with a welcome email sequence. See <a href="/academy/courses/landing-pages-lead-magnets/">Landing Pages &amp; Lead Magnets</a> and our <a href="/academy/welcome-email-sequence-examples/">welcome email sequence examples</a>.</p>
<h2>Turn DMs into customers</h2>
<ol>
<li><strong>Thank and ask:</strong> "Thanks for reaching out! Is this for you or a gift?"</li>
<li><strong>Understand the need</strong> with one or two questions.</li>
<li><strong>Recommend one option</strong> with the price or next step.</li>
<li><strong>Make it easy:</strong> send the booking or checkout link.</li>
<li><strong>Follow up once</strong> if they go quiet — politely, after a day or two.</li>
</ol>
<p>Save these as quick replies so anyone on your team can answer consistently.</p>
<h2>Partnerships and user-generated content</h2>
<p>Collaborate with local businesses or small creators whose audience matches yours — a joint giveaway, a shared post or a guest video. Ask happy customers for permission to share their photos and reviews; real customers are often more convincing than polished brand content. Remember to disclose any paid or gifted partnership clearly.</p>
<h2>Protect your community</h2>
<p>Set simple house rules: hide or delete spam and abusive comments, use the platform's keyword filters to block common spam words, and never share a customer's personal details in public. A friendly, safe comment section encourages more people to join the conversation.</p>""",
"example": "<p>A home-organising business posted a carousel called \"The 10-minute kitchen reset\" ending with \"Comment 'RESET' for the printable checklist\". Each comment got a personal DM with a link to a one-field sign-up page, followed by a three-email welcome sequence with a booking offer. The post itself earned engagement, and the email list turned that attention into paid consultations long after the post stopped being shown.</p>",
"checklist": "I reply to genuine comments and DMs every day\nI engage on other relevant accounts each week\nEvery post has one call to action that fits its goal\nI have a lead magnet and a simple landing page\nNew sign-ups get a welcome email sequence\nI have saved quick replies for common DM questions\nI ask happy customers for permission to share their content",
"assignment": "<p>Create a lead magnet idea for your business and write the post that promotes it (hook, value, \"comment a keyword\" or \"link in bio\" call to action). Then write three saved replies for your most common DM questions.</p>",
"video_script": "Hook: The checklist post that kept bringing clients after it stopped trending.\nSocial is social: reply, engage, handle complaints.\nCalls to action for each goal.\nMove followers to your email list with a lead magnet.\nThe five-step DM conversation.\nPartnerships and customer content.\nAssignment: lead magnet post and three saved replies.",
"quiz": [
  {"q": "Why move social followers onto an email list?", "opts": ["Platforms ban businesses that don't", "You own the list and can reach people directly", "Emails are always opened", "It increases your follower count"], "correct": 1, "exp": "Followers belong to the platform; an email list is an audience you control."},
  {"q": "Someone sends a DM asking about prices. What should you do first?", "opts": ["Ignore it until the weekend", "Thank them and ask a question to understand their need", "Send your full price list with no message", "Ask them to call during office hours only"], "correct": 1, "exp": "A quick, friendly reply with a question starts a sales conversation while interest is high."},
  {"q": "How should you handle a public complaint?", "opts": ["Delete it immediately", "Argue the facts in the comments", "Acknowledge it calmly and move details to a private message", "Block the person"], "correct": 2, "exp": "A calm public response shows other customers you care; private messages handle the details."},
]})

L.append({"module": 1, "title": "Measuring social media results: metrics that matter", "slug": "measuring-social-media-results", "minutes": 11, "free_preview": False,
"intro": "Likes feel good but do not pay the bills. Learn which social media metrics actually show progress toward your goal, where to find them, and how to run a 30-minute monthly review that tells you what to do next.",
"body": """<h2>Three levels of metrics</h2>
<table>
<thead><tr><th>Level</th><th>Metrics</th><th>Question it answers</th></tr></thead>
<tbody>
<tr><td>Reach</td><td>Views, reach, accounts reached, non-follower reach</td><td>Are new people seeing my content?</td></tr>
<tr><td>Engagement</td><td>Watch time, saves, shares, comments, profile visits</td><td>Do people find it useful enough to act?</td></tr>
<tr><td>Business results</td><td>Link clicks, DMs, leads, bookings, sales</td><td>Is social media helping the business?</td></tr>
</tbody>
</table>
<p>Always connect your report to the business goal you set in Lesson 1. Reach and engagement are leading signals; business results are the score.</p>
<h2>Useful ratios</h2>
<ul>
<li><strong>Engagement rate</strong> = (likes + comments + shares + saves) ÷ reach (or views). Platforms and tools calculate it differently, so always compare with your own past posts using the same formula.</li>
<li><strong>Saves and shares per post:</strong> strong signs that content is genuinely useful.</li>
<li><strong>Profile visit → link click rate</strong> = link clicks ÷ profile visits. If it is low, improve your bio and link.</li>
<li><strong>Click → lead rate</strong> = leads ÷ link clicks. If it is low, improve your landing page or offer.</li>
</ul>
<h2>Where to find the numbers</h2>
<ul>
<li><strong>Platform insights</strong> (free with business accounts): Instagram and Facebook insights in the app or Meta Business Suite, LinkedIn Page analytics, TikTok analytics, YouTube Studio.</li>
<li><strong>Google Analytics 4:</strong> visits and conversions that came from social. Tag every link with UTM parameters, for example <code>?utm_source=instagram&amp;utm_medium=social&amp;utm_campaign=spring-offer</code>. New to GA4? Take <a href="/academy/courses/ga4-for-beginners/">GA4 for Beginners</a>.</li>
<li><strong>Your CRM, booking tool or spreadsheet:</strong> ask new customers "How did you hear about us?" and record the answer. Many social sales happen through DMs that analytics never sees.</li>
</ul>
<h2>The 30-minute monthly review</h2>
<ol>
<li><strong>Collect</strong> the month's numbers in one sheet: posts published, reach, saves, shares, profile visits, link clicks, DMs, leads and sales.</li>
<li><strong>Rank your posts</strong> by the metric closest to your goal (for example, DMs or link clicks), not by likes.</li>
<li><strong>Find patterns</strong> in your top three: which pillar, format, hook and topic?</li>
<li><strong>Find the leak:</strong> lots of reach but few profile visits? Improve hooks and calls to action. Visits but no clicks? Fix the bio. Clicks but no leads? Fix the landing page.</li>
<li><strong>Decide</strong> one thing to do more of, one to stop and one new test for next month.</li>
</ol>
<h2>Avoid these traps</h2>
<ul>
<li>Judging a post after one hour — give it at least a few days.</li>
<li>Comparing yourself with huge accounts instead of your own last month.</li>
<li>Chasing viral reach that brings the wrong audience.</li>
<li>Changing strategy every week before you have enough posts to learn from.</li>
</ul>
<h2>Set targets from your own baseline</h2>
<p>There is no universal "good" engagement rate or reach number — it varies by platform, industry and account size. Use your first full month as a baseline, then set modest targets for the next month, such as more saves per post or more DMs from your call to action. Steady improvement on your own numbers is the goal.</p>
<p>When you know which posts bring leads, you also know which ones to put money behind later — the best organic posts are often the best first ads.</p>""",
"example": "<p>A wedding florist noticed her most-liked posts were finished bouquets, but her monthly review showed that DMs and enquiries mostly came from short \"how we plan your flowers\" videos with a clear \"DM 'DATE' to check availability\" call to action. She made the planning videos a weekly pillar and tagged her bio link with UTMs. The next month's review showed more enquiries from fewer total likes.</p>",
"checklist": "I track reach, engagement and business results — not only likes\nMy report is connected to my 90-day goal\nI use the same engagement-rate formula every month\nEvery link from social has UTM tags\nI ask new customers how they heard about us\nI run a 30-minute review each month and choose one test",
"assignment": "<p>Build a monthly review sheet with columns for posts, reach, saves, shares, profile visits, link clicks, DMs, leads and sales. Fill it in for last month (or set target numbers if you are just starting) and write one \"do more\", one \"stop\" and one \"test\" decision.</p>",
"video_script": "Hook: Her most-liked posts weren't the ones bringing bookings.\nThree levels of metrics.\nRatios that show where the leak is.\nWhere to find the numbers — and UTM tags.\nThe 30-minute monthly review.\nTraps to avoid.\nAssignment: build your review sheet.",
"quiz": [
  {"q": "Which metric is closest to business results?", "opts": ["Likes", "Follower count", "Leads from social", "Number of hashtags used"], "correct": 2, "exp": "Leads, bookings and sales show whether social media is actually helping the business."},
  {"q": "You get lots of profile visits but very few link clicks. What should you improve first?", "opts": ["Your bio and link", "Your posting time", "Your hashtags", "Your profile photo filter"], "correct": 0, "exp": "Visitors arrive but don't click — the bio and link aren't giving them a clear, compelling next step."},
  {"q": "Why ask new customers \"How did you hear about us?\"", "opts": ["It is a legal requirement", "Sales that start in DMs or word of mouth often don't show in analytics", "It replaces Google Analytics", "It increases engagement rate"], "correct": 1, "exp": "Many social sales happen in messages or offline, so asking fills the gaps analytics can't see."},
]})

# Final project lesson (kind "project", no quiz) — every course ends with one.
L.append({"module": 2, "kind": "project", "title": "Final project: your 30-day social media plan", "slug": "social-media-plan-project", "minutes": 45, "free_preview": False,
"intro": "Bring everything together in a 30-day social media plan for a real or imaginary small business. It is practical proof of your skills for clients, employers or your own business.",
"body": "<h2>What to include</h2><ol><li><strong>Goal and customer:</strong> one 90-day business goal and a short description of the target customer.</li><li><strong>Platforms:</strong> one or two platforms and why they fit this customer and business.</li><li><strong>Profile:</strong> the name field, three-line bio with a call to action, link destination (with UTM tags) and pinned posts or highlights.</li><li><strong>Content pillars:</strong> 3–4 pillars with an example post for each.</li><li><strong>30-day calendar:</strong> at least 12 posts with date, platform, pillar, format, hook and call to action.</li><li><strong>Three finished posts:</strong> fully written — hook, script or slides, caption and call to action.</li><li><strong>Leads plan:</strong> your lead magnet or offer, landing page, DM process and saved replies.</li><li><strong>Measurement:</strong> the metrics you will review at the end of the month and the target for each.</li></ol><h2>How it is reviewed</h2><p>A good plan is specific (real hooks, real offers, real dates), consistent (every post supports the goal and pillars) and realistic for the time the business actually has each week.</p>",
"example": "<p>A neighbourhood coffee shop plan: goal — 150 new loyalty-app sign-ups in 90 days. Platforms — Instagram for locals and a Facebook Page for community events. Pillars — \"behind the bar\", \"coffee tips\", \"regular of the week\" and \"this week's offer\". Twelve Reels and carousels over 30 days, a \"comment 'BEANS' for a free pastry with your first app order\" post, and a monthly review of reach, saves, DMs, sign-ups and redemptions.</p>",
"checklist": "My goal is a business result, not a vanity metric\nI explained why I chose my platforms\nMy profile has a clear bio, link and call to action\nI have 3–4 pillars with examples\nMy calendar has at least 12 planned posts\nThree posts are fully written\nI have a plan to turn followers into leads\nI listed the metrics and targets I will review",
"assignment": "<p>Submit your 30-day plan (document, spreadsheet, PDF or link). Keep the strategy part to one or two pages and put the calendar in a simple table — clarity beats length.</p>",
"video_script": "Hook: A 30-day plan that proves you can run social media.\nWhat to include, section by section.\nExample: the coffee shop plan.\nHow it is reviewed.\nSubmit your plan.",
"quiz": []})

for l in L:
    course["modules"][l.pop("module")]["lessons"].append(l)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "social-media-marketing-for-beginners.json")
json.dump(course, open(out, "w"), ensure_ascii=False, indent=2)
print("lessons:", sum(len(m["lessons"]) for m in course["modules"]), "quiz questions:", sum(len(l["quiz"]) for m in course["modules"] for l in m["lessons"]))
