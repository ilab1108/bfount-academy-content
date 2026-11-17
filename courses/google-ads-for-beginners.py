# Builds courses/google-ads-for-beginners.json (kept as Python for readable multi-line HTML).
import json, os

course = {
  "title": "Google Ads for Beginners",
  "slug": "google-ads-for-beginners",
  "category_id": 2,
  "level": "beginner",
  "icon": "🔎",
  "sort_order": 200,
  "summary": "Launch and manage your first profitable Google Search campaign: account structure, keywords and match types, ads that get clicks, bidding, budgets, tracking and weekly optimisation.",
  "outcomes": "\n".join([
    "Explain how the Google Ads auction and Ad Rank decide who shows and what they pay",
    "Structure a Search campaign with tightly themed ad groups",
    "Choose keywords, match types and negative keywords that protect your budget",
    "Write responsive search ads and assets that earn clicks",
    "Pick a bidding strategy and budget that fit your data and goals",
    "Track conversions and run a simple weekly optimisation routine",
  ]),
  "description": "<p>Google Ads puts your business in front of people at the exact moment they search for what you sell. It is also one of the fastest ways to waste money if you set it up carelessly. This course shows you how to do it properly from day one.</p><p>You will learn how the auction works, how to structure a Search campaign, pick keywords and match types, write ads that get clicks, choose bidding and budgets, set up conversion tracking and improve results every week. Every lesson has a real-world example, a checklist and a small assignment, and the course ends with a complete campaign plan you can launch.</p>",
  "project": "Write a launch-ready Google Search campaign plan for a real or imaginary business: the goal and maximum cost per lead, campaign settings (locations, networks, budget), 2–3 ad groups with keywords and match types, a starting negative keyword list, one responsive search ad per ad group with assets, the bidding strategy and when you will change it, conversion tracking, and your weekly optimisation checklist.",
  "status": "published",
  "modules": [
    {"title": "Module 1 · How Google Ads works", "lessons": []},
    {"title": "Module 2 · Build, track and optimise", "lessons": []},
    {"title": "Module 3 · Your first campaign plan", "lessons": []},
  ],
}

L = []

L.append({"module": 0, "title": "How Google Ads works: the auction, Ad Rank and campaign types", "slug": "how-google-ads-works", "minutes": 11, "free_preview": True,
"intro": "Every time someone searches on Google, an instant auction decides which ads show, in what order and what each advertiser pays. In this lesson you will learn how that auction works and which campaign type a beginner should start with.",
"body": """<h2>Paying for intent</h2>
<p>Google Search ads show when someone types a search that matches your keywords. You usually pay only when someone <strong>clicks</strong> (cost per click, CPC). Because people are actively looking, search traffic often converts better than ads that interrupt a feed.</p>
<h2>The auction in plain words</h2>
<p>The highest bid does not automatically win. Google calculates an <strong>Ad Rank</strong> for each eligible ad, based mainly on:</p>
<ul>
<li><strong>Your bid</strong> — the most you are willing to pay for a click.</li>
<li><strong>Ad quality</strong> — how likely the ad is to be clicked, how relevant it is to the search and how good the landing page is.</li>
<li><strong>Context</strong> — the search itself, the device, location and time, and the expected impact of your assets (sitelinks, calls and so on).</li>
</ul>
<p>Higher-quality ads can show above competitors who bid more, and often pay less per click. Quality is a money-saver, not a nice-to-have.</p>
<h2>The main campaign types</h2>
<table>
<thead><tr><th>Type</th><th>Where ads show</th><th>Good for</th></tr></thead>
<tbody>
<tr><td>Search</td><td>Google search results</td><td>Capturing people who already want what you sell — the best place to start</td></tr>
<tr><td>Performance Max</td><td>Across Google (Search, YouTube, Display, Gmail, Maps, Discover)</td><td>Accounts with solid conversion tracking and data</td></tr>
<tr><td>Shopping</td><td>Product listings with images and prices</td><td>Online shops with a product feed</td></tr>
<tr><td>Display / Demand Gen</td><td>Websites, apps, YouTube and Discover feeds</td><td>Awareness and remarketing</td></tr>
<tr><td>Video</td><td>YouTube</td><td>Awareness and consideration with video</td></tr>
</tbody>
</table>
<h2>Account structure</h2>
<p><strong>Account → campaigns → ad groups → keywords and ads.</strong> Budgets, locations and bidding live at campaign level. Each ad group holds one tight theme of keywords with ads written for that theme.</p>""",
"example": "<p>Two dentists bid on \"emergency dentist near me\". One bids more but sends clicks to a generic home page with a vague ad. The other bids less, but the ad says \"Same-Day Emergency Appointments\" and links to an emergency page with a phone number. The second dentist often shows higher and pays less per click, because Google expects searchers to find that ad more useful.</p>",
"checklist": "I can explain why the highest bid doesn't always win\nI know the main parts of Ad Rank\nI know why Search is the best first campaign type\nI understand account → campaign → ad group → keywords and ads",
"assignment": "<p>Search Google for three things your business (or a business you know) sells. Note which advertisers show, what their headlines promise and where they send you. Write one thing each does well and one thing you would do better.</p>",
"video_script": "Hook: The dentist who bid less and still won.\nPaying for intent: CPC on search.\nAd Rank: bid, quality, context.\nCampaign types and why to start with Search.\nAccount structure.\nAssignment: study three live auctions.",
"quiz": [
  {"q": "What mainly decides whose ad shows first?", "opts": ["Only the highest bid", "Ad Rank, combining bid, ad quality and context", "Who has the oldest account", "Who spends the most per month"], "correct": 1, "exp": "Ad Rank combines your bid with ad quality and context, so a better ad can beat a higher bid."},
  {"q": "Which campaign type is usually best for a beginner's first campaign?", "opts": ["Display", "Search", "Video", "App"], "correct": 1, "exp": "Search captures people who are already looking, and it is the easiest to control and learn from."},
  {"q": "Where are budgets and locations set?", "opts": ["On each keyword", "On each ad", "At campaign level", "In Google Analytics"], "correct": 2, "exp": "Budget, location, network and bidding settings live at campaign level."},
]})

L.append({"module": 0, "title": "Keywords, match types and negative keywords", "slug": "keywords-and-match-types", "minutes": 13, "free_preview": False,
"intro": "Keywords decide which searches can trigger your ads. Match types decide how closely a search must match. Negative keywords stop the wrong searches. Getting these three right is the biggest budget saver in Google Ads.",
"body": """<h2>Start from the customer's words</h2>
<p>List what people type when they are ready to buy: the service, the problem, the location and urgency words. Then expand with the free <strong>Keyword Planner</strong> in Google Ads to see related ideas and rough search volumes and bids.</p>
<h2>Keyword intent</h2>
<ul>
<li><strong>High intent:</strong> "emergency plumber leeds", "buy running shoes flat feet", "accountant near me".</li>
<li><strong>Research:</strong> "how to fix a leaking tap", "best running shoes" — cheaper but less likely to buy now.</li>
<li><strong>Wrong intent:</strong> "plumber jobs", "free plumbing course" — not customers at all.</li>
</ul>
<h2>The three match types</h2>
<table>
<thead><tr><th>Match type</th><th>Written as</th><th>Matches</th></tr></thead>
<tbody>
<tr><td>Exact</td><td>[emergency plumber]</td><td>Searches with the same meaning as the keyword — the tightest control</td></tr>
<tr><td>Phrase</td><td>"emergency plumber"</td><td>Searches that include the meaning of the keyword, e.g. "emergency plumber in leeds"</td></tr>
<tr><td>Broad</td><td>emergency plumber</td><td>Searches related to the keyword — the widest reach, best used with smart bidding and good conversion data</td></tr>
</tbody>
</table>
<p>For a small first budget, start with <strong>exact and phrase match</strong> on your best keywords. Add broad match later, once conversion tracking is working and you can see which searches convert.</p>
<h2>Negative keywords</h2>
<p>Negative keywords block searches you don't want. Build a starting list before launch: <em>jobs, careers, salary, free, course, training, DIY, how to</em> (if you sell the service, not the information), and competitors' or unrelated product names. Then check the <strong>search terms report</strong> every week and add new negatives.</p>
<h2>Group keywords into tight themes</h2>
<p>Put 5–20 closely related keywords in each ad group (for example "emergency plumber" separate from "boiler repair") so every ad can speak directly to the search.</p>""",
"example": "<p>A driving school bidding on broad \"driving lessons\" found in the search terms report that a large share of clicks came from \"driving instructor jobs\" and \"driving theory test free\". Adding <em>jobs, instructor, free</em> and <em>theory</em> as negatives, and moving the best searches to phrase and exact match, cut wasted spend and lowered their cost per booking.</p>",
"checklist": "My keywords are the words ready-to-buy customers use\nI start with exact and phrase match on a small budget\nI have a starting negative keyword list before launch\nEach ad group has one tight keyword theme\nI review the search terms report every week",
"assignment": "<p>Use Keyword Planner (or brainstorm) to pick 10 high-intent keywords for one product or service. Mark each as exact or phrase, group them into two ad groups, and write 15 negative keywords.</p>",
"video_script": "Hook: The driving school paying for job seekers.\nThe customer's words and Keyword Planner.\nHigh intent, research and wrong intent.\nExact, phrase and broad.\nNegative keywords and the search terms report.\nTight ad groups.\nAssignment: 10 keywords, 2 ad groups, 15 negatives.",
"quiz": [
  {"q": "Which match type gives the tightest control over which searches show your ad?", "opts": ["Broad", "Phrase", "Exact", "Negative"], "correct": 2, "exp": "Exact match only shows for searches with the same meaning as your keyword."},
  {"q": "A carpet cleaner's ads show for \"carpet cleaning jobs\". What should they do?", "opts": ["Raise the bid", "Add \"jobs\" as a negative keyword", "Switch to broad match", "Pause the campaign"], "correct": 1, "exp": "A negative keyword blocks searches from job seekers who will never become customers."},
  {"q": "Where do you see the actual searches that triggered your ads?", "opts": ["Keyword Planner", "The search terms report", "The billing page", "Google Business Profile"], "correct": 1, "exp": "The search terms report lists the real searches people typed before clicking."},
]})

L.append({"module": 0, "title": "Writing ads that get clicks: responsive search ads and assets", "slug": "writing-google-search-ads", "minutes": 12, "free_preview": False,
"intro": "Your ad is the only thing a searcher sees before deciding to click. Learn how responsive search ads work, how to write headlines and descriptions that stand out, and which assets make your ad bigger and more useful.",
"body": """<h2>How responsive search ads work</h2>
<p>A responsive search ad (RSA) lets you write up to <strong>15 headlines</strong> (30 characters each) and <strong>4 descriptions</strong> (90 characters each). Google mixes and matches them to show the best combination for each search. Aim for at least 8–10 distinct headlines and all 4 descriptions.</p>
<h2>What to write</h2>
<ul>
<li><strong>The keyword theme</strong> in a few headlines, so the ad clearly matches the search.</li>
<li><strong>The offer:</strong> price, free quote, discount, free trial.</li>
<li><strong>Proof:</strong> years in business, reviews, number of customers, guarantees.</li>
<li><strong>Speed and convenience:</strong> "Same-Day Service", "Book Online in 60 Seconds".</li>
<li><strong>A clear call to action:</strong> "Call Now", "Get Your Free Quote".</li>
</ul>
<p>Make headlines genuinely different from each other — ten versions of the same sentence give Google nothing to test. Use <strong>pinning</strong> sparingly; it limits combinations.</p>
<h2>Ad strength</h2>
<p>Google rates each RSA from Poor to Excellent. Use it as a hint for variety, not a goal in itself. Real results — click-through rate and conversions — matter more.</p>
<h2>Assets (formerly extensions)</h2>
<table>
<thead><tr><th>Asset</th><th>What it adds</th></tr></thead>
<tbody>
<tr><td>Sitelinks</td><td>Extra links to pages like Pricing, Reviews, Contact</td></tr>
<tr><td>Callouts</td><td>Short benefits: "No Call-Out Fee", "Licensed &amp; Insured"</td></tr>
<tr><td>Structured snippets</td><td>Lists such as Services: Repairs, Installation, Maintenance</td></tr>
<tr><td>Call</td><td>A phone number or call button — vital for pay-per-call and local services</td></tr>
<tr><td>Location</td><td>Your address from Google Business Profile</td></tr>
<tr><td>Image</td><td>A relevant image alongside the ad</td></tr>
</tbody>
</table>
<p>Assets make your ad larger and more useful and contribute to Ad Rank, so add every one that fits.</p>
<h2>Match the landing page</h2>
<p>Send each ad group to a page that continues the same promise. If the ad says "Free Same-Day Quote", the page must show how to get it immediately.</p>""",
"example": "<p>An HVAC company's ad read \"Quality Heating Services — Call Us Today\". Rewritten headlines like \"Boiler Repair Today\", \"No Call-Out Fee\", \"4.9★ From 600+ Reviews\" and \"Fixed Price Before We Start\", plus sitelinks and a call asset, made the ad far more specific than competitors' and raised its click-through rate.</p>",
"checklist": "Each RSA has 8–15 distinct headlines and 4 descriptions\nHeadlines include the keyword theme, offer, proof and a call to action\nI pin only when it is really needed\nSitelinks, callouts and a call asset are added where they fit\nEach ad group sends clicks to a matching landing page",
"assignment": "<p>For one ad group from the last lesson, write 10 headlines (max 30 characters), 4 descriptions (max 90 characters), 4 sitelinks and 4 callouts.</p>",
"video_script": "Hook: 'Quality services, call today' — why that ad loses.\nHow RSAs mix headlines and descriptions.\nKeyword, offer, proof, speed, call to action.\nAd strength is a hint, not a goal.\nAssets that make your ad bigger.\nMatching landing pages.\nAssignment: write a full RSA.",
"quiz": [
  {"q": "How many headlines can a responsive search ad have?", "opts": ["Up to 3", "Up to 5", "Up to 15", "Unlimited"], "correct": 2, "exp": "An RSA can have up to 15 headlines of up to 30 characters each."},
  {"q": "Why should headlines be genuinely different from each other?", "opts": ["Google rejects similar headlines", "So Google has real variations to test and combine", "It lowers your bid automatically", "It is required for call assets"], "correct": 1, "exp": "Distinct headlines give the system real options to find the best combination."},
  {"q": "Which asset is most important for a business that wants phone calls?", "opts": ["Image asset", "Structured snippet", "Call asset", "Price asset"], "correct": 2, "exp": "A call asset adds a phone number or call button directly to the ad."},
]})

L.append({"module": 1, "title": "Bidding strategies and budgets", "slug": "google-ads-bidding-and-budgets", "minutes": 12, "free_preview": False,
"intro": "Your bidding strategy tells Google what to optimise for; your budget sets how much it may spend. Learn which strategy fits a new campaign, when to switch to smart bidding, and how daily budgets actually behave.",
"body": """<h2>Know your target first</h2>
<p>Work out your <strong>maximum cost per lead</strong> (or cost per sale) before choosing a bid strategy. If a customer is worth $600 in profit and 1 in 4 leads becomes a customer, you can pay up to $150 per lead to break even. Your real target should be lower so you make a profit.</p>
<h2>The main bidding strategies</h2>
<table>
<thead><tr><th>Strategy</th><th>What it does</th><th>When to use it</th></tr></thead>
<tbody>
<tr><td>Manual CPC</td><td>You set the max bid per keyword</td><td>Very small budgets or when you want full control while learning</td></tr>
<tr><td>Maximize clicks</td><td>Gets as many clicks as possible for the budget</td><td>Brand-new campaigns gathering early data (set a max CPC limit)</td></tr>
<tr><td>Maximize conversions</td><td>Gets as many conversions as possible for the budget</td><td>Once conversion tracking works and conversions are coming in</td></tr>
<tr><td>Target CPA</td><td>Aims for an average cost per conversion you set</td><td>Steady conversion volume (roughly 15–30+ a month)</td></tr>
<tr><td>Maximize conversion value / Target ROAS</td><td>Optimises for revenue or return on ad spend</td><td>Shops and businesses that track conversion values</td></tr>
</tbody>
</table>
<p>Smart bidding strategies (Maximize conversions, Target CPA, Target ROAS) learn from your conversion data, so they are only as good as your tracking. After switching, allow a <strong>learning period</strong> of one to two weeks before judging results and avoid big daily changes.</p>
<h2>How daily budgets work</h2>
<ul>
<li>Your daily budget is an <strong>average</strong>. On busy days Google can spend up to twice the daily budget, but over a month it won't charge more than about 30.4 times the daily budget.</li>
<li>Start with a budget that can buy enough clicks to learn: a common rule is enough for at least 10–20 clicks a day at your expected CPC.</li>
<li>Spread too little budget over too many campaigns and none of them gets enough data. Fewer, better-funded campaigns learn faster.</li>
</ul>
<h2>Key settings to check</h2>
<ul>
<li><strong>Networks:</strong> untick the Display Network in a Search campaign.</li>
<li><strong>Locations:</strong> choose "Presence" (people in or regularly in your area) rather than people who are only interested in it.</li>
<li><strong>Ad schedule:</strong> if you want calls, show ads only when someone can answer the phone.</li>
</ul>""",
"example": "<p>A legal firm launched with Maximize conversions on day one, before its form tracking worked. Google had nothing to learn from and spent the budget on cheap, poor-quality clicks. After fixing tracking, running Maximize clicks with a CPC limit for three weeks and then switching to Maximize conversions, their cost per enquiry settled close to their target.</p>",
"checklist": "I know my maximum and target cost per lead\nMy bid strategy matches how much conversion data I have\nI give smart bidding a learning period before judging it\nMy budget can buy enough clicks each day to learn\nDisplay Network is off and locations are set to Presence\nAd schedule matches when we can answer calls",
"assignment": "<p>Calculate your break-even and target cost per lead. Choose a starting bid strategy, a daily budget and the point (number of conversions) at which you will switch strategies. Write one sentence explaining each choice.</p>",
"video_script": "Hook: The law firm that let Google bid blind.\nYour maximum cost per lead.\nManual, clicks, conversions, target CPA, target ROAS.\nThe learning period.\nHow daily budgets really behave.\nThree settings to check.\nAssignment: pick your strategy and budget.",
"quiz": [
  {"q": "Why can Maximize conversions perform badly in a brand-new account?", "opts": ["It is only for shops", "It needs working conversion tracking and data to learn from", "It always overspends the monthly budget", "It turns off negative keywords"], "correct": 1, "exp": "Smart bidding learns from conversions; without tracked conversions it is guessing."},
  {"q": "Your daily budget is $50. What is the most Google normally charges over a month?", "opts": ["$50", "About $1,520", "$3,000", "There is no limit"], "correct": 1, "exp": "The monthly charging limit is about 30.4 × the daily budget: 30.4 × $50 ≈ $1,520."},
  {"q": "A customer is worth $600 profit and 1 in 4 leads buys. What is the break-even cost per lead?", "opts": ["$60", "$150", "$600", "$2,400"], "correct": 1, "exp": "$600 × 1/4 = $150 per lead at break-even."},
]})

L.append({"module": 1, "title": "Conversion tracking: know which clicks make money", "slug": "google-ads-conversion-tracking", "minutes": 12, "free_preview": False,
"intro": "Without conversion tracking you are judging Google Ads by clicks — and clicks don't pay the bills. Learn what to track, how to set it up and how to check it works before you spend serious money.",
"body": """<h2>What counts as a conversion?</h2>
<p>A conversion is an action that is valuable to your business. Choose one or two <strong>primary</strong> actions to optimise for and keep softer actions as secondary:</p>
<ul>
<li><strong>Primary:</strong> purchases, lead form submissions, booked appointments, phone calls longer than a set duration.</li>
<li><strong>Secondary:</strong> newsletter sign-ups, brochure downloads, clicks on a map.</li>
</ul>
<h2>Ways to track</h2>
<table>
<thead><tr><th>Method</th><th>Tracks</th></tr></thead>
<tbody>
<tr><td>Google tag (directly or via Google Tag Manager)</td><td>Form submits, thank-you pages, purchases on your site</td></tr>
<tr><td>Import from Google Analytics 4</td><td>Key events you already track in GA4</td></tr>
<tr><td>Calls from ads</td><td>Calls from your call asset, using a Google forwarding number</td></tr>
<tr><td>Calls from website</td><td>Calls from a phone number shown on your site after an ad click</td></tr>
<tr><td>Offline conversion import</td><td>Leads that later became sales in your CRM</td></tr>
</tbody>
</table>
<p>Turn on <strong>enhanced conversions</strong> where you can; it uses hashed first-party data (like email) to measure more accurately when cookies are limited.</p>
<h2>Test before you trust</h2>
<ol>
<li>Submit a test form or make a test purchase.</li>
<li>Check the tag fires using Google Tag Assistant.</li>
<li>Confirm the conversion action shows as "Recording conversions" within a day or so.</li>
<li>Make sure each conversion is counted once (set leads to "One" per click, purchases to "Every").</li>
</ol>
<h2>Track quality, not just quantity</h2>
<p>A cheap lead that never buys is expensive. Mark leads as qualified or sold in your CRM and import those results back into Google Ads when you can, so bidding learns which clicks bring real customers.</p>""",
"example": "<p>A roofing company counted every thank-you page view as a lead — including people who refreshed the page. Their reported cost per lead looked great but sales were flat. After setting the lead action to count \"One\" per click, adding call tracking with a minimum call length and importing sold jobs from their CRM, they could finally see which keywords produced paying customers.</p>",
"checklist": "I have one or two primary conversion actions\nForms, calls and purchases are tracked\nEnhanced conversions are on where possible\nI tested each conversion and saw it recorded\nLeads count once per click; purchases count every time\nI plan to import qualified leads or sales from my CRM",
"assignment": "<p>List every action on your site that matters (forms, calls, purchases, bookings). Mark each as primary or secondary, choose a tracking method for each and write how you will test it.</p>",
"video_script": "Hook: The roofer whose 'great' leads never bought.\nPrimary vs secondary conversions.\nGoogle tag, GA4 import, call tracking, offline import.\nEnhanced conversions.\nTest before you trust.\nTrack quality, not just quantity.\nAssignment: map your conversions.",
"quiz": [
  {"q": "Which is the best primary conversion for a local service business?", "opts": ["Page views", "Lead form submissions and qualified calls", "Time on site", "Social shares"], "correct": 1, "exp": "Primary conversions should be actions that directly lead to revenue."},
  {"q": "How should a lead form conversion usually be counted?", "opts": ["Every", "One per click", "Only on weekends", "Never"], "correct": 1, "exp": "Counting one per click stops repeat submissions inflating lead numbers."},
  {"q": "Why import sales from your CRM into Google Ads?", "opts": ["It lowers the CPC automatically", "So bidding learns which clicks bring real customers", "It is required to run ads", "It removes the need for a website"], "correct": 1, "exp": "Offline imports teach smart bidding the difference between cheap leads and profitable customers."},
]})

L.append({"module": 1, "title": "Reading results and optimising every week", "slug": "google-ads-weekly-optimisation", "minutes": 12, "free_preview": False,
"intro": "A Google Ads campaign is never finished. Learn which metrics matter, how to diagnose problems, and a simple 30-minute weekly routine that steadily lowers your cost per lead.",
"body": """<h2>The metrics that matter</h2>
<table>
<thead><tr><th>Metric</th><th>Formula</th><th>What it tells you</th></tr></thead>
<tbody>
<tr><td>Click-through rate (CTR)</td><td>Clicks ÷ impressions</td><td>Is the ad relevant and appealing?</td></tr>
<tr><td>Cost per click (CPC)</td><td>Cost ÷ clicks</td><td>How competitive the auction is and how good your quality is</td></tr>
<tr><td>Conversion rate</td><td>Conversions ÷ clicks</td><td>Do the landing page and offer persuade?</td></tr>
<tr><td>Cost per conversion (CPA)</td><td>Cost ÷ conversions</td><td>Are you under your target?</td></tr>
<tr><td>ROAS</td><td>Conversion value ÷ cost</td><td>Revenue earned per unit of spend</td></tr>
<tr><td>Impression share</td><td>Shown ÷ eligible impressions</td><td>How much of the market you are missing, and whether budget or rank is the cause</td></tr>
</tbody>
</table>
<h2>Diagnose by symptom</h2>
<ul>
<li><strong>Low CTR:</strong> ads don't match the search — tighten ad groups, rewrite headlines, add assets.</li>
<li><strong>High CPC:</strong> competition or low quality — improve ad relevance and landing page, check Quality Score.</li>
<li><strong>Clicks but no conversions:</strong> landing page, offer or tracking problem — test the page and the tag.</li>
<li><strong>Lost impression share (budget):</strong> good campaign held back — raise budget if CPA is on target.</li>
</ul>
<h2>Quality Score</h2>
<p>Each keyword gets a 1–10 Quality Score based on <strong>expected CTR</strong>, <strong>ad relevance</strong> and <strong>landing page experience</strong>. It is a diagnostic: a "below average" rating tells you which of the three to fix.</p>
<h2>The 30-minute weekly routine</h2>
<ol>
<li><strong>Search terms:</strong> add negatives for irrelevant searches; add strong converting searches as keywords.</li>
<li><strong>Keywords:</strong> pause or lower bids on keywords well over target CPA with enough data.</li>
<li><strong>Ads:</strong> replace low-performing headlines; keep testing new angles.</li>
<li><strong>Budget:</strong> move money from weak campaigns to campaigns beating target.</li>
<li><strong>Landing page:</strong> check it loads fast on a phone and the form or phone number works.</li>
<li><strong>Note</strong> what you changed and why, so next week you can judge the result.</li>
</ol>
<p>Change a few things at a time and give changes enough clicks to judge. Daily tinkering resets learning and hides what actually worked.</p>""",
"example": "<p>A wedding venue saw a strong CTR but no enquiries. The search terms report showed many clicks from \"wedding venue jobs\" and \"cheap wedding venues free\", and the enquiry form was broken on mobile. Adding negatives and fixing the form brought their cost per enquiry down sharply within a month — without raising the budget.</p>",
"checklist": "I know CTR, CPC, conversion rate, CPA, ROAS and impression share\nI diagnose problems by symptom before changing things\nI use Quality Score components to find what to fix\nI run the 30-minute routine every week\nI log every change and why I made it",
"assignment": "<p>Using real data or the sample numbers in the lab (2,000 impressions, 120 clicks, $360 cost, 9 conversions), calculate CTR, CPC, conversion rate and CPA. Then write the first three actions from the weekly routine you would take.</p>",
"video_script": "Hook: Great click-through, zero enquiries — what went wrong.\nSix metrics and their formulas.\nDiagnose by symptom.\nQuality Score as a diagnostic.\nThe 30-minute weekly routine.\nDon't tinker daily.\nAssignment: calculate and plan.",
"quiz": [
  {"q": "120 clicks cost $360 and produced 9 conversions. What is the cost per conversion?", "opts": ["$3", "$30", "$40", "$360"], "correct": 2, "exp": "$360 ÷ 9 = $40 per conversion."},
  {"q": "Your ads get lots of clicks but no conversions. What should you check first?", "opts": ["The landing page, offer and conversion tracking", "Your logo", "Raising the budget", "Adding the Display Network"], "correct": 0, "exp": "Clicks without conversions point to the page, the offer or broken tracking."},
  {"q": "Which three components make up Quality Score?", "opts": ["Bid, budget and location", "Expected CTR, ad relevance and landing page experience", "Impressions, clicks and cost", "Ad strength, assets and schedule"], "correct": 1, "exp": "Quality Score reflects expected CTR, ad relevance and landing page experience."},
]})

# Final project lesson (kind "project", no quiz) — every course ends with one.
L.append({"module": 2, "kind": "project", "title": "Final project: your launch-ready Google Search campaign plan", "slug": "google-ads-campaign-plan-project", "minutes": 45, "free_preview": False,
"intro": "Bring everything together in a complete Search campaign plan for a real or imaginary business — ready to build in Google Ads and proof of your skills for clients or employers.",
"body": "<h2>What to include</h2><ol><li><strong>Goal and numbers:</strong> the conversion you want, customer value, close rate, break-even and target cost per lead.</li><li><strong>Campaign settings:</strong> locations (Presence), networks (Search only), ad schedule and daily budget.</li><li><strong>Ad groups and keywords:</strong> 2–3 tight ad groups with 5–20 keywords each, marked exact or phrase.</li><li><strong>Negative keywords:</strong> a starting list of at least 20.</li><li><strong>Ads and assets:</strong> one responsive search ad per ad group (10+ headlines, 4 descriptions), plus sitelinks, callouts and a call asset if calls matter.</li><li><strong>Landing pages:</strong> which page each ad group uses and why it matches.</li><li><strong>Bidding:</strong> starting strategy and the point at which you will switch to smart bidding.</li><li><strong>Tracking:</strong> primary and secondary conversions, how each is tracked and how you tested it.</li><li><strong>Optimisation:</strong> your weekly routine and the metrics you will report.</li></ol><h2>How it is reviewed</h2><p>A strong plan is specific (real keywords, real numbers), tight (each ad group, ad and page share one theme), safe (negatives, Presence targeting, tracking tested before spend) and realistic for the budget.</p>",
"example": "<p>A mobile phone repair shop plan: goal is booked repairs at under $25 each. Search-only campaign within 10 km, open hours only, $30 a day. Ad groups: screen repair, battery replacement, water damage — each with exact and phrase keywords and its own landing page. Negatives include <em>jobs, course, DIY, how to, free</em>. RSAs promise \"Same-Day Screen Repair\" with reviews and price callouts. Maximize clicks with a CPC limit until 20 tracked bookings, then Maximize conversions. Weekly search-terms review and CPA report.</p>",
"checklist": "My target cost per lead is calculated\nSettings: Search only, Presence targeting, sensible schedule and budget\n2–3 tight ad groups with match types\nAt least 20 negative keywords\nA full RSA and assets for each ad group\nMatching landing pages\nA bidding plan with a switch point\nTested conversion tracking\nA weekly optimisation routine",
"assignment": "<p>Submit your campaign plan (document, spreadsheet, PDF or link). A clear table of ad groups, keywords and ads is better than long paragraphs.</p>",
"video_script": "Hook: A plan you could launch tomorrow.\nNumbers first: target cost per lead.\nSettings, ad groups, negatives.\nAds, assets and landing pages.\nBidding and tracking.\nExample: the phone repair shop.\nSubmit your plan.",
"quiz": []})

for l in L:
    course["modules"][l.pop("module")]["lessons"].append(l)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "google-ads-for-beginners.json")
json.dump(course, open(out, "w"), ensure_ascii=False, indent=2)
print("lessons:", sum(len(m["lessons"]) for m in course["modules"]), "quiz questions:", sum(len(l["quiz"]) for m in course["modules"] for l in m["lessons"]))
