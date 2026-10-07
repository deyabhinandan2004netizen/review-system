import random
from datetime import datetime, timedelta
from typing import List
from backend.schemas import ReviewItem

# Realistic seed reviews containing genuine, template duplicates, temporal bursts, and AI synthetic bots
now = datetime.now()

SAMPLE_REVIEWS_CATALOG = {
    # Case 1: Dropshipped Earbuds (Bot Spammed)
    "b09xs7jwhh|dropshipped earbuds": [
        ReviewItem(
            id="bot-ear-01",
            author="PrimeBuyer_991",
            rating=5.0,
            date=(now - timedelta(days=1)).strftime("%Y-%m-%d"),
            title="AMAZING EARBUDS BEST PURCHASE EVER",
            text="THIS IS A GAME CHANGER AND A TESTAMENT TO INNOVATION! Exceeded all my expectations in every aspect, look no further 5 stars all the way!!!!!!",
            verified_purchase=False,
            platform="Amazon"
        ),
        ReviewItem(
            id="bot-ear-02",
            author="ShopSaver_442",
            rating=5.0,
            date=(now - timedelta(days=1)).strftime("%Y-%m-%d"),
            title="BEST EVER MUST BUY",
            text="THIS IS A GAME CHANGER AND A TESTAMENT TO INNOVATION! Exceeded all my expectations in every aspect, look no further 5 stars all the way!!!!!!",
            verified_purchase=False,
            platform="Amazon"
        ),
        ReviewItem(
            id="bot-ear-03",
            author="DealHunter_77",
            rating=5.0,
            date=(now - timedelta(days=1)).strftime("%Y-%m-%d"),
            title="Pure perfection great quality",
            text="THIS IS A GAME CHANGER AND A TESTAMENT TO INNOVATION! Exceeded all my expectations in every aspect, look no further 5 stars all the way!!!!!!",
            verified_purchase=False,
            platform="Amazon"
        ),
        ReviewItem(
            id="bot-ear-04",
            author="SuperReviewerX",
            rating=5.0,
            date=(now - timedelta(days=1)).strftime("%Y-%m-%d"),
            title="A must buy for all",
            text="Extremely great loved it so much will recommend to everyone. 5 stars best earbuds ever!!! Top notch quality guaranteed!",
            verified_purchase=False,
            platform="Flipkart"
        ),
        ReviewItem(
            id="bot-ear-05",
            author="QuickReviewer_01",
            rating=5.0,
            date=(now - timedelta(days=1)).strftime("%Y-%m-%d"),
            title="good good good",
            text="good good good very nice product good quality",
            verified_purchase=False,
            platform="Amazon"
        ),
        ReviewItem(
            id="bot-ear-06",
            author="PromoSeeker99",
            rating=5.0,
            date=(now - timedelta(days=2)).strftime("%Y-%m-%d"),
            title="Got 150 cashback on paytm",
            text="Gave 5 stars to get 150 cashback on Paytm as told by seller in packaging slip card. Nice earbuds.",
            verified_purchase=False,
            platform="Amazon"
        ),
        ReviewItem(
            id="bot-ear-07",
            author="Rahul Verma",
            rating=1.0,
            date=(now - timedelta(days=6)).strftime("%Y-%m-%d"),
            title="Do not buy! Cheap Chinese clone",
            text="Terrible quality waste of money broke immediately! Left earbud stopped charging after 2 days. Total scam and no customer support.",
            verified_purchase=True,
            platform="Amazon"
        ),
        ReviewItem(
            id="bot-ear-08",
            author="Pooja Sharma",
            rating=2.0,
            date=(now - timedelta(days=9)).strftime("%Y-%m-%d"),
            title="Disappointing sound and poor mic",
            text="Sound is muffled and microphone does not pick up voice during Zoom calls. Bluetooth connection drops frequently. Not worth the money.",
            verified_purchase=True,
            platform="Flipkart"
        ),
        ReviewItem(
            id="bot-ear-09",
            author="AI_Review_Bot_01",
            rating=5.0,
            date=(now - timedelta(days=1)).strftime("%Y-%m-%d"),
            title="Unparalleled acoustic brilliance",
            text="Cannot recommend enough! Seamlessly blends cutting-edge technology with pure perfection. A beacon of modern audio engineering!",
            verified_purchase=False,
            platform="Amazon"
        ),
        ReviewItem(
            id="bot-ear-10",
            author="SpeedBuyer_55",
            rating=5.0,
            date=(now - timedelta(days=1)).strftime("%Y-%m-%d"),
            title="Super item",
            text="Extremely great loved it so much will recommend to everyone. 5 stars best earbuds ever!!! Top notch quality guaranteed!",
            verified_purchase=False,
            platform="Flipkart"
        )
    ],

    # Case 2: Sony WH-1000XM5 (Genuine Reviews)
    "sony wh-1000xm5|sony": [
        ReviewItem(
            id="rev-001",
            author="Aditya Sharma",
            rating=5.0,
            date=(now - timedelta(days=2)).strftime("%Y-%m-%d"),
            title="Unbeatable ANC for frequent travelers",
            text="The active noise cancellation is leagues ahead of my older XM3s. Flight engine rumble is completely vanished. Soundstage is rich, bass is deep yet punchy. Battery easily lasted through my 24h trip.",
            verified_purchase=True,
            platform="Amazon"
        ),
        ReviewItem(
            id="rev-002",
            author="Rohit Verma",
            rating=4.0,
            date=(now - timedelta(days=5)).strftime("%Y-%m-%d"),
            title="Great sound, but foldability is missed",
            text="Sound quality is crisp and microphone clarity on Zoom calls is drastically improved. My only gripe is the headband doesn't fold inward like the XM4, so the carrying case is quite bulky.",
            verified_purchase=True,
            platform="Flipkart"
        ),
        ReviewItem(
            id="rev-003",
            author="Priya Patel",
            rating=5.0,
            date=(now - timedelta(days=8)).strftime("%Y-%m-%d"),
            title="Premium build & all day comfort",
            text="Soft leatherette cushions make wearing these for 6+ hours painless. Multipoint connection between my MacBook and phone is seamless.",
            verified_purchase=True,
            platform="Croma"
        ),
        ReviewItem(
            id="rev-004",
            author="Kunal Malhotra",
            rating=4.0,
            date=(now - timedelta(days=14)).strftime("%Y-%m-%d"),
            title="Solid daily driver with great battery",
            text="Auto ANC adjustment sometimes changes noise profile unexpectedly in windy conditions, but overall the acoustic isolation and build quality are top tier.",
            verified_purchase=True,
            platform="Amazon"
        ),
        ReviewItem(
            id="rev-005",
            author="Sneha Gupta",
            rating=5.0,
            date=(now - timedelta(days=18)).strftime("%Y-%m-%d"),
            title="Audiophile grade tuning with EQ tweaks",
            text="Out of the box the default sound is a bit bass-heavy, but tweaking the Sony Headphones Connect app EQ unlocks pristine mids and crystal highs. Worth every penny.",
            verified_purchase=True,
            platform="Amazon"
        ),
        ReviewItem(
            id="rev-006",
            author="Anand Joshi",
            rating=4.5,
            date=(now - timedelta(days=22)).strftime("%Y-%m-%d"),
            title="Impressive microphones",
            text="Eight beamforming microphones filter out kitchen blender and ambient coffee shop chatter remarkably well. Calls are super clean.",
            verified_purchase=True,
            platform="Croma"
        ),
        ReviewItem(
            id="rev-007",
            author="BotUser_Promo",
            rating=5.0,
            date=(now - timedelta(days=24)).strftime("%Y-%m-%d"),
            title="BEST PRODUCT EVER",
            text="THIS IS A GAME CHANGER AND A TESTAMENT TO INNOVATION! Exceeded all my expectations in every aspect, look no further 5 stars all the way!!!!!!",
            verified_purchase=False,
            platform="Walmart"
        ),
        ReviewItem(
            id="rev-008",
            author="Deepak Nair",
            rating=4.0,
            date=(now - timedelta(days=27)).strftime("%Y-%m-%d"),
            title="High price but delivers",
            text="At 30k rupees it is definitely an investment, but if you work in open offices or travel frequently, the peace of mind is worth the price.",
            verified_purchase=True,
            platform="Flipkart"
        )
    ],

    # Case 3: Ayurvedic Slimming Juice (Cashback Spam)
    "ayurvedic slimming juice|slimming juice|ayurvedic": [
        ReviewItem(
            id="slm-01",
            author="UserOffer_12",
            rating=5.0,
            date=(now - timedelta(days=1)).strftime("%Y-%m-%d"),
            title="Seller gave 100 rs cashback on whatsapp",
            text="Seller contacted on WhatsApp offering 100 rs cashback for 5 star rating. Product tastes sweet and okay. Got money immediately.",
            verified_purchase=False,
            platform="Amazon"
        ),
        ReviewItem(
            id="slm-02",
            author="BargainHunter_88",
            rating=5.0,
            date=(now - timedelta(days=1)).strftime("%Y-%m-%d"),
            title="Free gift cashback received",
            text="Seller contacted on WhatsApp offering 100 rs cashback for 5 star rating. Good delivery and nice bottle.",
            verified_purchase=False,
            platform="Amazon"
        ),
        ReviewItem(
            id="slm-03",
            author="WeightLossMagic_99",
            rating=5.0,
            date=(now - timedelta(days=1)).strftime("%Y-%m-%d"),
            title="Lost 10kg in 3 days miracle juice!",
            text="THIS IS A GAME CHANGER AND A TESTAMENT TO INNOVATION! Exceeded all my expectations in every aspect, look no further 5 stars all the way!!!!!!",
            verified_purchase=False,
            platform="Flipkart"
        ),
        ReviewItem(
            id="slm-04",
            author="SpamPromoter_1",
            rating=5.0,
            date=(now - timedelta(days=1)).strftime("%Y-%m-%d"),
            title="A must buy for all",
            text="THIS IS A GAME CHANGER AND A TESTAMENT TO INNOVATION! Exceeded all my expectations in every aspect, look no further 5 stars all the way!!!!!!",
            verified_purchase=False,
            platform="Amazon"
        ),
        ReviewItem(
            id="slm-05",
            author="Sunita Rao",
            rating=1.0,
            date=(now - timedelta(days=8)).strftime("%Y-%m-%d"),
            title="Useless sugar water, caused stomach cramps",
            text="Do not fall for these fake reviews! It is just flavored colored syrup with artificial preservatives. Did not lose an ounce and gave me severe heartburn.",
            verified_purchase=True,
            platform="Amazon"
        ),
        ReviewItem(
            id="slm-06",
            author="Rakesh Tiwari",
            rating=1.0,
            date=(now - timedelta(days=12)).strftime("%Y-%m-%d"),
            title="Fake reviews scam",
            text="Inside the box was a scratch card saying rate 5 stars and message this number for Paytm reward. Completely unverified and useless product.",
            verified_purchase=True,
            platform="Flipkart"
        ),
        ReviewItem(
            id="slm-07",
            author="FastDeal_001",
            rating=5.0,
            date=(now - timedelta(days=1)).strftime("%Y-%m-%d"),
            title="good good",
            text="good good good very nice product good",
            verified_purchase=False,
            platform="Amazon"
        )
    ],

    # Case 4: Anker Fast Charger (Authentic Feedback)
    "anker fast charger|anker|fast charger": [
        ReviewItem(
            id="ank-01",
            author="Vikram Sethi",
            rating=5.0,
            date=(now - timedelta(days=3)).strftime("%Y-%m-%d"),
            title="Compact powerhouse charges MacBook and iPhone together",
            text="GaN technology makes this tiny brick replace my bulky 67W Apple charger. Runs slightly warm under full 65W load but never throttles or drops connection. Sturdy foldable prongs make it perfect for carry-on.",
            verified_purchase=True,
            platform="Amazon"
        ),
        ReviewItem(
            id="ank-02",
            author="Arjun Nambiar",
            rating=4.5,
            date=(now - timedelta(days=7)).strftime("%Y-%m-%d"),
            title="Fast charging protocol support is unmatched",
            text="Supports Samsung Super Fast Charging 2.0 (PPS 45W) seamlessly. Build quality is solid matte finish that resists scratches. Only minor con is that plugging a second device briefly resets the power handshake for 1 second.",
            verified_purchase=True,
            platform="Amazon"
        ),
        ReviewItem(
            id="ank-03",
            author="Tanvi Mehta",
            rating=4.0,
            date=(now - timedelta(days=11)).strftime("%Y-%m-%d"),
            title="Premium adapter, worth the extra cost",
            text="A bit heavier in hand than cheaper local adapters, but thermal management and surge protection give peace of mind. Charges my Dell XPS laptop and iPad without any hiccups.",
            verified_purchase=True,
            platform="Croma"
        ),
        ReviewItem(
            id="ank-04",
            author="Siddharth Roy",
            rating=5.0,
            date=(now - timedelta(days=15)).strftime("%Y-%m-%d"),
            title="All day reliability for travelers",
            text="Replaced 3 separate wall adapters with this single unit. Fast delivery and pristine packaging from official retailer. Highly recommended.",
            verified_purchase=True,
            platform="Flipkart"
        ),
        ReviewItem(
            id="ank-05",
            author="Harsh Vardhan",
            rating=4.0,
            date=(now - timedelta(days=20)).strftime("%Y-%m-%d"),
            title="Good charger, slightly pricey",
            text="Great build quality and charging speed. At 3500 INR it is on the higher side, but the durability and GaN efficiency justify the value for money.",
            verified_purchase=True,
            platform="Amazon"
        )
    ]
}

def get_product_reviews(product_name: str) -> List[ReviewItem]:
    """
    Returns authentic + synthetic reviews for the given product.
    If not in catalog, dynamically generates a category-aware 10-12 review audit set.
    """
    clean_name = product_name.lower().strip()
    for keys, revs in SAMPLE_REVIEWS_CATALOG.items():
        key_list = keys.split("|")
        for k in key_list:
            if k in clean_name:
                return revs

    # Generate rich, realistic product-specific reviews (7-8 Real, 2-3 Fake Bots, 1 Suspicious)
    short_title = product_name.split(",")[0].split("(")[0].strip()
    if len(short_title) > 40:
        short_title = short_title[:38] + "..."

    t = clean_name
    is_audio = any(w in t for w in ["headphone", "earbud", "earphone", "audio", "airdope", "neckband", "speaker", "soundbar", "tws", "anc", "buds"])
    is_cooler = any(w in t for w in ["cooler", "cooling", "pad", "stand", "fan"])
    is_phone = any(w in t for w in ["iphone", "galaxy", "smartphone", "phone", "mobile", "pixel", "oneplus", "redmi", "realme"])
    is_laptop = any(w in t for w in ["macbook", "laptop", "thinkpad", "notebook", "dell", "hp", "asus", "acer", "lenovo"])
    is_watch = any(w in t for w in ["watch", "smartwatch", "fitness", "band", "tracker"])
    is_health = any(w in t for w in ["juice", "ayurvedic", "detox", "slimming", "protein", "supplement", "vitamin", "health"])

    if is_cooler:
        real_reviews = [
            ("Sunil Sharma", 5.0, 4, "Significant temperature drop during heavy gaming", f"Tested {short_title} with my RTX gaming laptop. CPU and GPU temperatures dropped by 6-8°C during heavy sessions. The 5 fans push noticeable airflow while remaining whisper quiet under 21 dBA.", "Amazon"),
            ("Megha Sengupta", 4.0, 11, "Sturdy build, great ergonomic height angles", f"The 5 height angle adjustments relieve neck and wrist strain during long work hours. The dual USB pass-through ports are very convenient so I don't lose a port on my laptop.", "Flipkart"),
            ("Varun Pillai", 5.0, 17, "RGB lighting looks slick and LCD display is handy", f"The LCD display allows fine-tuning fan speeds easily. Holds my 15.6-inch laptop securely without slipping. Solid metal mesh construction.", "Amazon"),
            ("Deepika Joshi", 4.0, 24, "Effective cooling, quiet operation", f"Noticeable cooling effect when rendering 4K video clips. Fans run smoothly without high-pitched whirring. Very satisfied with the airflow and aesthetic lighting.", "Croma"),
            ("Rohan Mehta", 5.0, 32, "Reliable cooling pad for everyday workloads", f"Keeps laptop cool and prevents thermal throttling during extended sessions. Braided USB cable included in box is durable and good quality.", "Amazon"),
            ("Aarav Desai", 4.0, 41, "Good airflow, lightweight to move around desk", f"Blows cool air directly across laptop intake vents. Rubber anti-skid stoppers hold the machine firmly even at steep angles.", "Flipkart"),
            ("Nisha Nair", 5.0, 49, "Excellent value for money, fast delivery", f"Delivered within 2 days with intact packaging. Very effective cooling pad for budget and mid-tier gaming setups.", "Amazon")
        ]
    elif is_audio:
        real_reviews = [
            ("Rohit Sharma", 5.0, 4, "Impressive bass and battery endurance", f"Been using {short_title} daily for over 2 weeks. The drivers deliver punchy, distortion-free bass and vocals remain crystal clear. Battery easily lasts 6-7 hours on a single charge and case charges quickly via Type-C.", "Amazon"),
            ("Priya Patel", 4.0, 11, "Great value, mic is decent indoors", f"The Bluetooth 5.3 connection is instant and stays connected across rooms. Microphones work fine in quiet rooms, though in heavy traffic background noise can bleed in. Very solid value for money.", "Flipkart"),
            ("Vikram Malhotra", 5.0, 17, "Comfortable fit during gym workouts", f"Ergonomics on {short_title} are very well thought out. Does not slip out during running or gym sessions. Passive noise isolation is effective even in busy gyms.", "Amazon"),
            ("Ananya Deshmukh", 4.0, 24, "Clear audio, slight latency in fast FPS games", f"Music and streaming playback are flawless. Latency in videos is imperceptible, though in fast FPS mobile gaming there is a tiny split-second lag. Overall thoroughly satisfied.", "Croma"),
            ("Karan Singhania", 5.0, 31, "Superb build quality and pocketable case", f"Case finish feels durable and hinge has a satisfying snap. Pairing with both my phone and laptop was immediate. Outstanding audio quality in this segment.", "Amazon"),
            ("Sneha Roy", 4.0, 39, "Balanced soundstage and reliable controls", f"Touch gestures took a day to get used to, but respond reliably. Sound signature has balanced highs and mid-range without harsh sibilance.", "Flipkart"),
            ("Aditya Kulkarni", 5.0, 48, "Prompt delivery and genuine product", f"Delivered within 24 hours with intact factory seals. Sounds noticeably richer than older budget earphones. Highly recommended for daily travel.", "Amazon")
        ]
    elif is_phone:
        real_reviews = [
            ("Amitabh Sen", 5.0, 3, "Exceptional display and fluid performance", f"The screen on {short_title} is breathtaking with deep contrast and vibrant colors. Apps launch instantaneously and multitasking with heavy apps is completely lag-free.", "Amazon"),
            ("Meenakshi Iyer", 4.0, 9, "Stunning low-light camera, battery lasts 1.5 days", f"Primary camera captures exceptional detail and natural skin tones even in dim lighting. Easily delivers 7+ hours of screen-on time with mixed usage.", "Flipkart"),
            ("Siddharth Jain", 5.0, 16, "Solid premium chassis and fast charging", f"Hand-feel is extremely premium with slim bezels and solid tactile buttons. Fast charging reaches 60% in under 30 minutes with the compatible adapter.", "Amazon"),
            ("Radhika Menon", 4.0, 22, "Great daily driver, slight warmth during gaming", f"Handles everyday tasks effortlessly. Phone gets slightly warm around the camera module during extended gaming sessions, but frame rates remain rock solid.", "Croma"),
            ("Nikhil Verma", 5.0, 30, "Clean software experience and great haptics", f"Operating system is snappy and free of bloatware. Haptic feedback during typing and navigation is crisp and precise.", "Amazon"),
            ("Tanvi Bhatt", 4.0, 38, "Crisp stereo speakers and loud calls", f"Earpiece call clarity is top notch even in crowded metro stations. Dual stereo speakers have good volume without cracking at max level.", "Flipkart"),
            ("Harsh Vardhan", 5.0, 46, "Worth every rupee for long term use", f"Upgraded after 3 years and the difference in camera quality and battery efficiency is massive. Delivered on time with secure tamper-proof packaging.", "Amazon")
        ]
    elif is_laptop:
        real_reviews = [
            ("Rakesh Nair", 5.0, 4, "Blazing fast workflow and silent thermals", f"The processor handles heavy code compilation and 4K editing effortlessly on {short_title}. Thermals stay exceptionally cool and fans rarely spin up under standard load.", "Amazon"),
            ("Divya Sundaram", 5.0, 10, "Battery easily powers through a full workday", f"Unplugged at 9 AM and still had 30% battery remaining by 7 PM. Display resolution and brightness make outdoor working effortless.", "Flipkart"),
            ("Sanjay Kulkarni", 4.0, 18, "Crisp keyboard travel and large precision trackpad", f"Keyboard has great tactile feedback for long typing sessions. Port selection is slightly minimal so dongles are needed, but performance is unbeatable.", "Croma"),
            ("Pooja Hegde", 5.0, 25, "Compact form factor with exceptional build", f"Solid aluminum unibody that feels extremely rigid with zero deck flex. Speakers sound surprisingly rich with good low-end depth for a thin laptop.", "Amazon"),
            ("Gaurav Kapoor", 4.0, 33, "Fast SSD boot times and sharp webcam", f"Boots in under 5 seconds from cold start. 1080p webcam and dual mics deliver clear audio during Zoom and Teams client conferences.", "Flipkart"),
            ("Arunav Das", 5.0, 42, "Best productivity investment this year", f"Seamless performance and lightweight enough to carry in backpack all day without feeling strained. Screen anti-reflective coating works great.", "Amazon"),
            ("Sunita Rao", 4.0, 51, "Reliable performance for everyday multitasking", f"Handles 30+ browser tabs, spreadsheets, and video calls simultaneously without throttling. Truly dependable machine.", "Amazon")
        ]
    elif is_health:
        real_reviews = [
            ("Dr. Rajesh Gupta", 5.0, 5, "Authentic herbal formulation and gentle on stomach", f"Ingredients in {short_title} are genuinely pure without synthetic fillers. Digestion improved noticeably within 10 days of regular morning consumption.", "Amazon"),
            ("Sunita Aggarwal", 4.0, 12, "Noticeable energy boost and reduced bloating", f"Natural herbal taste without artificial sweeteners. Helped curb mid-day cravings and reduced bloating significantly. Will reorder.", "Flipkart"),
            ("Manoj Tiwari", 5.0, 19, "Pure Ayurvedic quality and well packaged", f"Bottle came tightly sealed with dosage instructions clearly printed. Feels refreshing and natural when consumed with lukewarm water.", "Amazon"),
            ("Kavita Joshi", 4.0, 26, "Good natural supplement, takes time for visible results", f"Patience is needed as herbal products take 3-4 weeks to show cumulative benefits, but energy levels and bowel regularity have improved.", "Amazon"),
            ("Vipin Chandra", 5.0, 35, "Trusted daily health routine", f"Very clean product with lab-tested certification. Does not cause acidity or throat irritation like cheaper brands.", "Flipkart"),
            ("Preeti Sethi", 4.0, 44, "Authentic taste and effective detox", f"Subtle taste that indicates absence of added sugar or artificial colorants. Delivered in protective bubble packaging.", "Croma"),
            ("Anil Saxena", 5.0, 52, "Very satisfied with consistency and freshness", f"Batch manufacturing date was just 3 weeks ago. Fresh and high potency botanical blend.", "Amazon")
        ]
    else:
        # General tech / consumer electronics
        real_reviews = [
            ("Aman Mehra", 5.0, 4, "Exceeded all expectations in daily performance", f"The build quality and engineering on {short_title} are remarkable. Reliable performance, simple setup, and fast delivery.", "Amazon"),
            ("Deepak Rao", 4.0, 11, "Solid reliability and great value for money", f"Very well constructed overall. Minor cosmetic finish could be slightly refined, but functional performance and speed are top notch.", "Flipkart"),
            ("Pooja Sen", 5.0, 18, "Durable, high quality, and seamless to use", f"Handles day-to-day usage effortlessly. Exactly as described in store specifications and delivered securely on time.", "Croma"),
            ("Sameer Khan", 4.0, 25, "Dependable product with good warranty support", f"Works straight out of the box with zero complications. Customer support answered my warranty registration inquiry promptly.", "Amazon"),
            ("Rashmi Trivedi", 5.0, 33, "Great design and high quality materials", f"Materials feel sturdy and resilient to daily wear. Performs consistently without unexpected glitches.", "Amazon"),
            ("Kartik Bansal", 4.0, 41, "Good value compared to pricier alternatives", f"Offers 90% of the premium features at a fraction of the cost. Very satisfied with the overall experience.", "Flipkart"),
            ("Bhavna Shah", 5.0, 50, "Excellent purchase, highly recommended", f"High quality construction and packaged thoroughly. Has held up well over weeks of continuous testing.", "Amazon")
        ]

    output_reviews: List[ReviewItem] = []
    
    # 1. Add Authentic Reviews
    for idx, (author, rating, days_ago, r_title, r_text, plat) in enumerate(real_reviews):
        output_reviews.append(
            ReviewItem(
                id=f"rev-auth-{idx+1:02d}",
                author=author,
                rating=rating,
                date=(now - timedelta(days=days_ago)).strftime("%Y-%m-%d"),
                title=r_title,
                text=r_text,
                verified_purchase=True,
                platform=plat
            )
        )

    # 2. Add Fake / Bot Reviews (Duplicate copy-paste templates + burst spike date)
    burst_date = (now - timedelta(days=2)).strftime("%Y-%m-%d")
    bot_template = "THIS IS A GAME CHANGER AND A TESTAMENT TO INNOVATION! Exceeded all my expectations in every aspect, look no further 5 stars all the way!!!!!!"

    output_reviews.append(
        ReviewItem(
            id="rev-bot-01",
            author="PrimeBuyer_991",
            rating=5.0,
            date=burst_date,
            title="AMAZING PURCHASE MUST BUY EVER",
            text=bot_template,
            verified_purchase=False,
            platform="Amazon"
        )
    )
    output_reviews.append(
        ReviewItem(
            id="rev-bot-02",
            author="SuperSaver_442",
            rating=5.0,
            date=burst_date,
            title="BEST EVER TOP NOTCH",
            text=bot_template,
            verified_purchase=False,
            platform="Amazon"
        )
    )

    # 3. Add Incentive / Cashback solicitation review
    output_reviews.append(
        ReviewItem(
            id="rev-bot-03",
            author="PromoHunter_88",
            rating=5.0,
            date=(now - timedelta(days=3)).strftime("%Y-%m-%d"),
            title="Gave 5 stars got cashback",
            text=f"Gave 5 stars to get 150 cashback on Paytm as stated on scratch card slip in packaging box. Nice {short_title}.",
            verified_purchase=False,
            platform="Amazon"
        )
    )

    # 4. Add Low-Entropy Suspicious Review
    output_reviews.append(
        ReviewItem(
            id="rev-susp-01",
            author="QuickReviewer_X",
            rating=5.0,
            date=burst_date,
            title="good good good",
            text="good good good very nice product good quality top notch quality guaranteed.",
            verified_purchase=False,
            platform="Flipkart"
        )
    )

    return output_reviews

