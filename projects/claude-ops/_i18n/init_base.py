#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extracts shared static assets (SVG map geometry, cartoon review avatars, Stripe links,
price tables, map arcs) into _i18n/shared.json, and writes the canonical base locale
dictionaries _i18n/locales/zh.json and _i18n/locales/en.json.
"""
import json
import os
import re

ROOT = "/Users/jason/workspace/junxinzhang.github.io/projects/claude-ops"
I18N_DIR = os.path.join(ROOT, "_i18n")
LOCALES_DIR = os.path.join(I18N_DIR, "locales")
os.makedirs(LOCALES_DIR, exist_ok=True)


def extract_shared():
    with open(os.path.join(ROOT, "en/index.html"), "r", encoding="utf-8") as f:
        en_lines = f.readlines()
    en_full = "".join(en_lines)

    # Lines 932..962 (1-indexed) -> 931..962 (0-indexed slice) are <svg ...>...</svg> + <canvas ...></canvas>
    # Verify boundaries dynamically so we never depend on hardcoded line offsets alone:
    start_idx = next(i for i, l in enumerate(en_lines) if '<svg viewBox="0 0 1120 510"' in l)
    end_idx = next(i for i, l in enumerate(en_lines) if 'id="map-photon-canvas"' in l)
    map_bg_block = "".join(en_lines[start_idx : end_idx + 1])

    # Extract the 6 review avatar SVGs
    avatars = re.findall(
        r'<div class="review-avatar" aria-hidden="true">\s*(<svg[\s\S]*?</svg>)\s*</div>',
        en_full,
    )
    assert len(avatars) == 6, f"Expected 6 review avatars, got {len(avatars)}"

    # Extract STRIPE_LINKS object literal as JSON
    m_stripe = re.search(r"var STRIPE_LINKS = (\{[\s\S]*?\});", en_full)
    assert m_stripe, "Could not find STRIPE_LINKS"
    stripe_raw = m_stripe.group(1)
    # Convert single-quoted JS dict to JSON
    stripe_links = dict(re.findall(r"'([^']+)'\s*:\s*'([^']+)'", stripe_raw))
    assert len(stripe_links) >= 180, f"Unexpected stripe_links count: {len(stripe_links)}"

    # Extract ARCS JSON array
    m_arcs = re.search(r"var ARCS = (\[.*?\]);", en_full)
    assert m_arcs, "Could not find ARCS"
    arcs = json.loads(m_arcs.group(1))

    prices = {
        "AUD": {"sym": "A$", "p": [149, 579, 1049], "orig20x": 1499, "team": [899, 3199, 5799], "biz": [1949, 6599, 11899], "upg": [479, 539, 999], "line": [8, 30], "s": [13.99, 43.99, 88.99, 224.99], "so": [14.99, 44.99, 89.99, 225.99]},
        "USD": {"sym": "$", "p": [99, 399, 699], "orig20x": 999, "team": [599, 2199, 3899], "biz": [1299, 4499, 7999], "upg": [329, 359, 679], "line": [5, 20], "s": [8.99, 28.99, 58.99, 148.99], "so": [9.99, 29.99, 59.99, 149.99]},
        "EUR": {"sym": "€", "p": [89, 349, 629], "orig20x": 899, "team": [539, 1949, 3499], "biz": [1169, 3999, 7199], "upg": [289, 329, 609], "line": [5, 19], "s": [8.49, 26.99, 54.99, 138.99], "so": [9.49, 27.99, 55.99, 139.99]},
        "NZD": {"sym": "NZ$", "p": [179, 699, 1199], "orig20x": 1799, "team": [1079, 3849, 6699], "biz": [2299, 7899, 13799], "upg": [569, 629, 1179], "line": [10, 37], "s": [14.99, 47.99, 94.99, 239.99], "so": [15.99, 48.99, 95.99, 240.99]},
        "CAD": {"sym": "C$", "p": [139, 549, 969], "orig20x": 1399, "team": [839, 2999, 5399], "biz": [1799, 6199, 10999], "upg": [449, 499, 939], "line": [8, 29], "s": [12.49, 39.99, 79.99, 204.99], "so": [13.49, 40.99, 80.99, 205.99]},
        "CNY": {"sym": "¥", "p": [719, 2899, 4999], "orig20x": 7199, "team": [4299, 15999, 27999], "biz": [9199, 32999, 56999], "upg": [2399, 2599, 4899], "line": [36, 139], "s": [65, 209, 419, 1059]},
        "SGD": {"sym": "S$", "p": [129, 499, 899], "orig20x": 1299, "team": [779, 2749, 4999], "biz": [1649, 5699, 10299], "upg": [409, 469, 869], "line": [7, 26], "s": [11.99, 38.99, 78.99, 198.99], "so": [12.99, 39.99, 79.99, 199.99]},
    }

    node_geom = {
        "AU": {"x": 544.6, "y": 419.3, "hq": True, "leader": "544.6,419.3 494.0,432.0 488.0,432.0", "anchor": "right", "ax": 488.0, "ry": 420.0, "ty": 436.2},
        "US": {"x": 822.6, "y": 175.9, "hq": False, "leader": "822.6,175.9 836.0,184.0 842.0,184.0", "anchor": "left", "ax": 842.0, "ry": 172.0, "ty": 188.2},
        "SG": {"x": 392.1, "y": 300.3, "hq": False, "leader": "392.1,300.3 344.0,314.0 338.0,314.0", "anchor": "right", "ax": 338.0, "ry": 302.0, "ty": 318.2},
        "MY": {"x": 385.2, "y": 294.4, "hq": False, "leader": "385.2,294.4 336.0,278.0 330.0,278.0", "anchor": "right", "ax": 330.0, "ry": 266.0, "ty": 282.2},
        "ID": {"x": 401.8, "y": 325.1, "hq": False, "leader": "401.8,325.1 356.0,350.0 350.0,350.0", "anchor": "right", "ax": 350.0, "ry": 338.0, "ty": 354.2},
        "JP": {"x": 507.5, "y": 183.5, "hq": False, "leader": "507.5,183.5 520.0,176.0 526.0,176.0", "anchor": "left", "ax": 526.0, "ry": 164.0, "ty": 180.2},
        "KH": {"x": 395.6, "y": 266.7, "hq": False, "leader": "395.6,266.7 354.0,242.0 348.0,242.0", "anchor": "right", "ax": 348.0, "ry": 230.0, "ty": 246.2},
        "NZ": {"x": 620.4, "y": 430.1, "hq": False, "leader": "620.4,430.1 632.0,432.0 638.0,432.0", "anchor": "left", "ax": 638.0, "ry": 420.0, "ty": 436.2},
        "CA": {"x": 820.3, "y": 131.7, "hq": False, "leader": "820.3,131.7 806.0,112.0 800.0,112.0", "anchor": "right", "ax": 800.0, "ry": 100.0, "ty": 116.2},
    }

    shared = {
        "map_bg_block": map_bg_block,
        "review_avatars": avatars,
        "stripe_links": stripe_links,
        "prices": prices,
        "arcs": arcs,
        "node_geom": node_geom,
    }
    with open(os.path.join(I18N_DIR, "shared.json"), "w", encoding="utf-8") as f:
        json.dump(shared, f, ensure_ascii=False, indent=2)
    print(f"Wrote shared.json ({len(stripe_links)} Stripe links, {len(avatars)} avatars)")


EN_LOCALE = {
    "meta": {
        "title": "Zaokit ClaudeOps — AI Makes the World Borderless | Frontier Productivity & Top-Tier Experience",
        "description": "Zaokit ClaudeOps: AI makes the world borderless — lighting up every city worldwide to bring the most advanced productivity and a top-tier experience to everyone. Isolated physical Mac Studio & Mac mini workstations across 9 native ISP regions (AU, US, SG, MY, ID, JP, KH, NZ, CA), enterprise BGP dedicated lines, up to 7×24h 1-on-1 engineering concierge, and 2TB–30TB cloud storage.",
        "keywords": "Zaokit ClaudeOps, AI Makes the World Borderless, Lighting Up Every City, Claude managed service, Claude Code, Mac cloud workstation, dedicated Mac Studio, AI engineering concierge",
        "og_title": "AI Makes the World Borderless — Frontier Productivity & Top-Tier Experience | Zaokit ClaudeOps",
        "og_description": "Lighting up every city worldwide · 9 native ISP compute hubs · High-spec physical Mac workstations · Enterprise BGP acceleration · Up to 7×24h 1-on-1 concierge ops.",
        "ld_description": "AI makes the world borderless — lighting up every city worldwide to bring the most advanced productivity and a top-tier experience to everyone: isolated workspace on physical high-spec Mac Studio & Mac mini across 9 native ISP regions, enterprise BGP acceleration, and up to 7x24h 1-on-1 concierge AI engineering support.",
        "offer_names": ["1x Standard", "5x Pro", "20x Ultimate"]
    },
    "nav": {
        "brand": "Zaokit ClaudeOps",
        "why": "Why",
        "service": "Service",
        "value": "Beyond Compute",
        "security": "Security",
        "reviews": "Reviews",
        "pricing": "Pricing",
        "storage": "Cloud Storage",
        "process": "Process",
        "faq": "FAQ",
        "lang_aria": "Switch language"
    },
    "hero": {
        "eyebrow": "GLOBAL VISION · Let AI Light Up Every City, Every Individual",
        "h1_main": "AI Makes the World Borderless",
        "h1_sub": "We bring the most advanced productivity & top-tier experience to everyone",
        "lead": "Frontier AI productivity should never be the privilege of a few. From Sydney, Silicon Valley, Tokyo and Singapore to Jakarta—we are lighting up native compute hubs city by city across the globe, pairing isolated physical Mac workstations, enterprise BGP dedicated lines and up to 7×24h 1-on-1 engineering care so every creator, developer and team can build without borders.",
        "cta_primary": "View pricing",
        "cta_secondary": "Email us",
        "mailto_enquiry_subject": "Zaokit ClaudeOps enquiry",
        "stats": [
            {"strong": "9 Countries Lit", "span": "AU · US · SG · MY · ID · JP · KH · NZ · CA"},
            {"strong": "Physical Macs", "span": "High-spec Mac Studio & Mac mini"},
            {"strong": "Top Experience", "span": "7×8h / 7×16h / 7×24h 1-on-1 care"},
            {"strong": "Isolated Space", "span": "Own macOS account · Dedicated on 20x+"},
            {"strong": "AU Entity", "span": "Australian registered · Stripe billing"}
        ]
    },
    "map": {
        "status_main": "9 Countries & 13+ Core Cities Lit",
        "status_em": "LIGHTING UP EVERY CITY",
        "meta_1": "Native ISP compute mesh",
        "meta_2": "Borderless BGP backbone",
        "meta_3": "Hover or click a city hub",
        "stage_aria": "Global 9-country native ISP network topology map",
        "hud_live": "● Live",
        "hud_label_city": "Metro hub",
        "hud_label_hw": "Hardware",
        "hud_val_hw": "Mac Studio / High-spec mini",
        "hud_label_route": "Backbone",
        "pills_aria": "Select region",
        "partner_pill": "✦ Global Co-Building · Serving All 8 Billion People",
        "partner_copy_html": "<strong>Bring your own machine &amp; share your resources — earn revenue while lighting up the possibility of dreams for others!</strong>",
        "partner_cta": "Bring Machine / Join Us →",
        "partner_mailto_subject": "Bring My Mac / Join Zaokit Global Compute Network",
        "partner_mailto_body": "Hi Jason, I'd love to share my resources and join the Zaokit Global Compute Network:\n\n1. Country / City:\n2. Collaboration mode (Bring my own Mac / Native broadband node / Regional partner):\n3. Mac specs & local ISP details:\n4. Contact details:",
        "nodes": {
            "AU": {"name": "Australia", "pill": "Australia ★", "short": "Australia", "city": "Sydney · Melbourne", "role": "★ Primary HQ Hub · Australian Entity", "route": "Premium BGP via HK · 0% packet loss"},
            "US": {"name": "United States", "pill": "United States", "short": "United States", "city": "Silicon Valley · LA", "role": "US West Coast Core Compute Hub", "route": "Trans-Pacific direct · Native ISP"},
            "SG": {"name": "Singapore", "pill": "Singapore", "short": "Singapore", "city": "Singapore", "role": "APAC Low-Latency Core Hub", "route": "Subsea cable crossroads · Ultra-low RTT"},
            "MY": {"name": "Malaysia", "pill": "Malaysia", "short": "Malaysia", "city": "Kuala Lumpur", "role": "SE Asia Native Broadband Node", "route": "MY–SG terrestrial link · Clean native IP"},
            "ID": {"name": "Indonesia", "pill": "Indonesia", "short": "Indonesia", "city": "Jakarta", "role": "SE Asia Archipelago Native ISP Node", "route": "SG–Jakarta & Indigo subsea links"},
            "JP": {"name": "Japan", "pill": "Japan", "short": "Japan", "city": "Tokyo · Osaka", "role": "East Asia Ultra-Low-Latency Node", "route": "~92ms measured · 0% packet loss"},
            "KH": {"name": "Cambodia", "pill": "Cambodia", "short": "Cambodia", "city": "Phnom Penh", "role": "Direct Terrestrial Low-RTT Node", "route": "~81ms terrestrial direct · 0% loss"},
            "NZ": {"name": "New Zealand", "pill": "New Zealand", "short": "New Zealand", "city": "Auckland", "role": "South Pacific Clean Native Node", "route": "Trans-Tasman & Hawaiki subsea links"},
            "CA": {"name": "Canada", "pill": "Canada", "short": "Canada", "city": "Vancouver · Toronto", "role": "North America Clean Broadband Node", "route": "North Pacific direct · High stability"}
        }
    },
    "why": {
        "tag": "Why",
        "h2": "The hard part of Claude was never the model",
        "sub": "What really drains your energy is the uncertainty that has nothing to do with your work.",
        "cards": [
            {"h3": "Painful set-up", "p": "From account sign-up to environment configuration, you figure out every step alone, with no one to fall back on."},
            {"h3": "Unstable runs", "p": "Every local machine is different, and long Claude Code tasks get cut off halfway through."},
            {"h3": "Billing hassles", "p": "Failed payments, plan changes and renewals eat into your time every month."},
            {"h3": "Lost time", "p": "Hours spent researching tools and troubleshooting should go into your real work."}
        ]
    },
    "service": {
        "tag": "Service",
        "h2": "Hand us the uncertainty. Keep the certainty.",
        "sub": "From set-up to day-to-day operations, fully managed and ready to use.",
        "cards": [
            {"h3": "Isolated workspace", "p": "Your own macOS account and workspace with isolated files and permissions, plus a dedicated whole-machine option on 20x. Your conversations and project data stay under your control."},
            {"h3": "High-spec Mac Studio & mini", "p": "Your own high-spec Mac Studio or high-spec Mac mini on local native broadband networks in Australia, the US, Singapore, Malaysia, Indonesia, Japan, Cambodia, New Zealand or Canada (never cheap shared cloud data centers). Account-level isolation (dedicated machine on 20x), stable for the long run."},
            {"h3": "Managed billing", "p": "Subscriptions, renewals and plan changes are all handled by us. Nothing for you to chase."},
            {"h3": "Tiered 1-on-1 Concierge", "p": "Direct 1-on-1 engineering support scaled to your plan: 7×8h (1x), 7×16h (5x), up to 7×24h round-the-clock private concierge (20x)."}
        ]
    },
    "value": {
        "tag": "Beyond Compute",
        "h2_html": "What you get is <em class=\"grad\">more than compute</em>",
        "sub": "The account and the machine are just the start. The real edge is having experts help you use AI the right way, more deeply and earlier than others.",
        "cards": [
            {"h3": "Top-tier compute & workstation", "p": "A dedicated AI engineering workspace configured and managed for you, running on a physical high-spec Mac Studio or Mac mini so long Claude Code tasks keep going."},
            {"h3": "Top-Tier 1-on-1 Concierge", "p": "Dedicated AI engineering guidance built for creators, developers, founders and teams alike. From Claude Code workflows, MCP and Skills set-up to shipping real projects, get 7×8h / 7×16h / 7×24h direct 1-on-1 support."},
            {"h3": "First-hand AI insights", "p": "Regular updates on new features, best practices and industry news for Claude and other leading AI tools, so you adopt new capabilities first."}
        ]
    },
    "network": {
        "tag": "Network",
        "h2_html": "Ongoing network investment<br>for a responsive remote desktop",
        "p": "We keep investing in hardware and premium routes: 9-country native ISP broadband with 200Mbps–500Mbps+ symmetrical speeds, paired with self-hosted relays and an enterprise BGP backbone that cut packet loss—the real enemy of remote desktops—to zero.",
        "chips": ["200–500Mbps+ Symmetrical", "Enterprise BGP backbone", "Self-hosted relays", "Dual-leg BBR", "Apple Silicon hardware encoding", "Allow-list hardening"],
        "addon_note_prefix": "Included free on 20x, Team & Business; 1x / 5x subscribers can add the ",
        "addon_note_link": "ClaudeOps Enterprise Dedicated Line (from $5/mo) ↓",
        "addon_note_suffix": "",
        "card_aria": "Measured latency and packet loss before and after optimisation",
        "legend_before": "Before",
        "legend_after": "After",
        "rows": [
            {"country": "Japan", "via": "Via HK backbone", "before": "128–184ms · 10% loss", "after": "~92ms · 0% loss"},
            {"country": "Australia", "via": "Via HK backbone", "before": "343–386ms · 25–33% loss", "after": "~240ms · 0% loss"},
            {"country": "Cambodia", "via": "Direct land cable", "before": "", "after": "~81ms · 0% loss"}
        ],
        "foot": "Measured from an East Asian client, November 2026. Your experience may vary with your network."
    },
    "security": {
        "tag": "Security & Privacy",
        "h2": "Two-tier isolation: separate accounts and dedicated machines",
        "sub": "Your terminal carries private source code, API keys in environment variables, database settings and business logic. Zaokit ClaudeOps uses two tiers of isolation: on 1x / 5x every user gets a separate macOS account accessed only via Apple Screen Sharing; on 20x you can enable a whole dedicated machine, isolated right down to the hardware.",
        "cards": [
            {"h3": "20x dedicated machine: hardware-level isolation", "p": "With dedicated mode enabled, the entire high-spec Mac Studio or Mac mini serves only you. Install any software, change system-level settings, and use any remote desktop tool, including RustDesk and third-party VNC."},
            {"h3": "1x / 5x separate account isolation", "p": "Every user has a separate macOS account with its own files and permissions, so history and project files stay private. Access is via Apple Screen Sharing only, which gives each account its own isolated desktop session that no one else can see."},
            {"h3": "You control access and encryption", "p": "Set your own access passwords and encryption policies. Our team handles connectivity and billing and does not actively access data in your account, except for maintenance, security incidents or troubleshooting you authorise."}
        ]
    },
    "reviews": {
        "tag": "Testimonials",
        "h2": "What real subscribers say",
        "sub": "To protect client privacy, all reviews use cartoon avatars and anonymized handles while preserving real feedback and subscription tiers.",
        "badge": "Anonymized · Verified",
        "stars_aria": "5 out of 5 stars",
        "items": [
            {
                "name": "M***",
                "role": "Cross-border AI Product Lead",
                "quote": "\"The enterprise tunnel is razor-sharp and ultra-smooth—even clearer than my local ToDesk. Coding and switching windows feel practically local. Fast, reliable, worth every penny—a top-tier experience.\"",
                "source": "Verified Chat Feedback",
                "plan": "5x Pro"
            },
            {
                "name": "C***",
                "role": "Senior Full-Stack Engineer",
                "quote": "\"My local network environment used to drop mid-session all the time. After moving to ClaudeOps 1x Standard with an isolated workspace and Claude Code running 24/7, it genuinely feels like 'the genius programmer is back' 😂. Zero billing or network headaches now.\"",
                "source": "Verified Chat Feedback",
                "plan": "1x Standard"
            },
            {
                "name": "Kyle W.",
                "role": "Quant R&D Lead",
                "quote": "\"Native ISP networks across 9 countries plus hardware-level isolation sold me. Our proprietary code and API keys stay on a dedicated Mac Studio—months of continuous uptime with zero interruptions.\"",
                "source": "Australia Node · Masked",
                "plan": "20x Flagship"
            },
            {
                "name": "L***",
                "role": "Indie Developer",
                "quote": "\"Same-day delivery right after Stripe checkout. My isolated macOS account came pre-configured with Claude Code and dev tools. Huge time-saver if you don't want to fight environment setup or cross-border billing.\"",
                "source": "Tokyo Node · Masked",
                "plan": "1x Standard"
            },
            {
                "name": "Sarah C.",
                "role": "Consulting Partner",
                "quote": "\"I'm not an ops person and didn't want to touch CLI setups. Having 7×16h 1-on-1 support plus managed Google Drive sync means I can connect from anywhere while travelling and pick up right where I left off.\"",
                "source": "Singapore Node · Masked",
                "plan": "5x Pro"
            },
            {
                "name": "A***",
                "role": "E-commerce Tech Director",
                "quote": "\"Our core engineers run multi-agent refactors and test suites overnight and review clean PRs every morning. Native Screen Sharing is crystal clear, and Jason's Telegram support replies almost instantly.\"",
                "source": "Telegram Feedback",
                "plan": "20x Flagship"
            }
        ],
        "note": "* To strictly protect client privacy and data security, all reviews are displayed with cartoon avatars and anonymized/masked names."
    },
    "pricing": {
        "tag": "Pricing",
        "h2": "Plans from solo to enterprise.",
        "sub_html": "Scale from individual workspaces to dedicated multi-Mac clusters. <strong>Pay annually for 10 months and get 2 months free</strong>.",
        "jump_line": "Dedicated Line ↓",
        "jump_ent": "Team & Business ↓",
        "billing_aria": "Choose billing cycle",
        "billing_month": "Monthly",
        "billing_year": "Annual",
        "billing_save_badge": "2 months free",
        "currency_aria": "Choose currency",
        "currencies": {
            "AUD": {"btn": "A$ AUD", "name": "AUD"},
            "USD": {"btn": "$ USD", "name": "USD"},
            "EUR": {"btn": "€ EUR", "name": "EUR"},
            "NZD": {"btn": "NZ$ NZD", "name": "NZD"},
            "CAD": {"btn": "C$ CAD", "name": "CAD"},
            "SGD": {"btn": "S$ SGD", "name": "SGD"},
            "CNY": {"btn": "¥ CNY", "name": "CNY"}
        },
        "solo_subscribe": "Subscribe",
        "solo_consult": "Questions? Email us →",
        "solo": [
            {
                "tier_b": "1x",
                "tier_span": "Standard",
                "desc": "For everyday chat, writing and light coding with a stable Claude.",
                "init_note": "Includes Claude environment · about A$5 / day",
                "features_html": [
                    "Base usage allowance",
                    "Dedicated workspace configuration",
                    "Mac mini physical environment",
                    "Fully managed subscription billing &amp; ops",
                    "Claude Code ready",
                    "<strong>7×8h</strong> 1-on-1 dedicated support",
                    "Separate macOS account · Apple Screen Sharing access"
                ],
                "mailto_subject": "Zaokit ClaudeOps enquiry - 1x Standard"
            },
            {
                "badge": "Most popular",
                "tier_b": "5x",
                "tier_span": "Pro",
                "desc": "For developers and creators who use Claude Code heavily every day.",
                "init_note": "Includes Claude environment · 5x usage, unit cost about 78% of 1x",
                "features_html": [
                    "5x the Standard usage allowance",
                    "Dedicated workspace configuration",
                    "High-spec Mac mini physical environment",
                    "Fully managed subscription billing &amp; ops",
                    "Room for long Claude Code tasks",
                    "<strong>7×16h</strong> priority 1-on-1 support",
                    "Separate macOS account · Apple Screen Sharing access"
                ],
                "mailto_subject": "Zaokit ClaudeOps enquiry - 5x Pro"
            },
            {
                "badge_promo": "Year-End Promo · Until Dec 31, 2026",
                "tier_b": "20x",
                "tier_span": "Ultimate",
                "desc": "For prolific builders, founders and power users running multiple agents around the clock.",
                "orig_title": "Regular price",
                "init_note": "Promo price stays on renewal · unit cost about 35% of 1x",
                "features_html": [
                    "20x the Standard usage allowance",
                    "Dedicated workspace configuration",
                    "High-spec Mac Studio / Mac mini · Dedicated machine option",
                    "Fully managed subscription billing &amp; ops",
                    "Multi-agent and parallel tasks",
                    "<strong>Top-tier 7×24h</strong> private concierge channel",
                    "Complimentary high-speed RustDesk channel",
                    "Complimentary Google Drive 6 TB storage included"
                ],
                "mailto_subject": "Zaokit ClaudeOps enquiry - 20x Ultimate"
            }
        ],
        "dedicated_line": {
            "h3_main": "ClaudeOps Enterprise Dedicated Line · Cross-Border Acceleration",
            "h3_pill": "Complimentary on 20x / Team / Business",
            "sub": "Optional add-on for 1x & 5x subscribers: route traffic over our enterprise BGP cross-border backbone with dual-leg BBR 0% packet-loss acceleration for ultra-responsive Screen Sharing & Claude Code (annual billing gets 2 months free).",
            "cards": [
                {
                    "code": "1x Dedicated Line",
                    "span": "Standard Acceleration · For 1x Standard",
                    "desc": "Enterprise BGP cross-border backbone + self-hosted encrypted low-latency relay + dual-leg BBR optimization, keeping daily Apple Screen Sharing, SSH & light Claude Code sessions jitter-free at peak hours.",
                    "init_note": "24/7 BGP zero-loss acceleration · Managed with plan",
                    "btn": "Add 1x Line →"
                },
                {
                    "code": "5x Dedicated Line",
                    "span": "Pro Acceleration · For 5x Pro (20% lower unit cost)",
                    "desc": "5× priority bandwidth quota + high-priority enterprise BGP QoS queue + dual-leg BBR 0% packet-loss guarantee, built for heavy real-time Claude Code sessions, large repo syncs & high-FPS remote desktops.",
                    "init_note": "5× priority throughput · High-priority BGP QoS",
                    "btn": "Add 5x Line →"
                }
            ]
        },
        "enterprise": {
            "divider": "Team & Business · Dedicated Multi-Seat Clusters",
            "switch_aria": "Choose team seat tier",
            "tier_pro": "All-Pro Seats (1x)",
            "tier_max": "All-Max Seats (5x)",
            "tier_max_badge": "Recommended",
            "tier_ultra": "All-Ultra Seats (20x)",
            "toolbar_html": "Start with uniform Pro, Max or Ultra seats — or mix &amp; match any time with self-serve <strong>per-seat upgrade add-ons</strong> below.",
            "team": {
                "init_badge": "5 × Max (5x) Seats · Dedicated Host",
                "sub": "5 Seats",
                "desc": "Built for startup pods, AI studios and research teams — a dedicated physical Mac host for your team with unified billing & admin control.",
                "init_note": "Includes 5 Max (5x) isolated seats · Dedicated Mac host & consolidated billing",
                "init_seat_li_html": "Includes <strong>5 Max (5x) engineering seats</strong> (separate Claude workspace &amp; macOS account per member)",
                "features_html": [
                    "<strong>Dedicated high-spec Mac Studio / Mac mini host</strong> exclusively for your team",
                    "Organisation-owned seat reassignment for onboarding/offboarding &amp; <strong>single consolidated invoice</strong>",
                    "Upgrade individual seats to Max (5x) or Ultra (20x) on demand at any time",
                    "<strong>7×24h</strong> dedicated team concierge group channel",
                    "Complimentary private high-speed RustDesk team channel"
                ],
                "init_storage_li": "Complimentary 12 TB team cloud storage (Google Drive / iCloud+)",
                "btn": "Subscribe Team",
                "consult": "Need extra seats or custom specs? Talk to us →",
                "mailto_subject": "Zaokit ClaudeOps enquiry - Team Plan"
            },
            "biz": {
                "init_badge": "Enterprise · 10 × Max (5x) Cluster",
                "sub": "10 Seats",
                "desc": "For scaling tech companies, quant & engineering orgs — dedicated multi-Mac physical clusters with 9-country dual-region deployment.",
                "init_note": "Includes 10 Max (5x) isolated seats · Dedicated multi-Mac cluster & VIP SLA",
                "init_seat_li_html": "Includes <strong>10 Max (5x) engineering seats</strong> (expandable to 50+ seats on demand)",
                "features_html": [
                    "<strong>Dedicated multi-unit Mac Studio / Mac mini physical cluster</strong>",
                    "Supports <strong>dual-region deployment &amp; rapid migration across 9 countries</strong> + dedicated static native ISP",
                    "Consolidated commercial invoicing &amp; dedicated Customer Success Manager",
                    "<strong>Top-tier 7×24h VIP enterprise SLA channel</strong> (priority ops &amp; architecture advisory)",
                    "Complimentary dedicated enterprise RustDesk relay line"
                ],
                "init_storage_li": "Complimentary 30 TB enterprise cloud storage (Google Drive / iCloud+)",
                "btn": "Subscribe Business",
                "consult": "20+ seats or custom private cluster? Contact enterprise sales →",
                "mailto_subject": "Zaokit ClaudeOps enquiry - Business Plan"
            }
        },
        "seat_addons": {
            "h3_main": "Per-Seat Upgrade Add-ons",
            "h3_pill": "1–50 seats adjustable at checkout",
            "sub": "Mix & match tiers on any active Team or Business base plan — upgrade specific members on demand (annual add-ons also get 2 months free).",
            "cards": [
                {
                    "from": "Pro 1x",
                    "to": "Max 5x",
                    "tag": "Upgrade",
                    "desc": "Upgrade any Pro (1x) team seat to Max (5x) for heavy daily Claude Code engineering.",
                    "btn": "Upgrade seat →"
                },
                {
                    "from": "Max 5x",
                    "to": "Ultra 20x",
                    "tag": "Upgrade",
                    "desc": "Upgrade founders, CTOs or lead architects on an All-Max plan to 20x Ultra multi-agent capacity.",
                    "btn": "Upgrade seat →"
                },
                {
                    "from": "Pro 1x",
                    "to": "Ultra 20x",
                    "tag": "Direct",
                    "desc": "Jump any seat on an All-Pro base plan straight to full 20x Ultra flagship allowance.",
                    "btn": "Upgrade seat →"
                }
            ]
        },
        "storage": {
            "tag": "Cloud Storage · Google Drive & iCloud+",
            "h2": "Managed Cloud Storage for Digital Assets",
            "sub_html": "Choose <strong>Google Drive (Google One)</strong> or <strong>Apple iCloud+</strong> across 2 TB to 30 TB tiers, with managed renewals and the same 7×16h 1-on-1 concierge support.",
            "currency_aria": "Choose currency (cloud storage)",
            "per_mo": "/ mo",
            "cards": [
                {
                    "tier_b": "2 TB",
                    "tier_span": "Storage",
                    "desc": "Generous storage for everyday photos, videos and cross-device backups.",
                    "note": "Google Drive or iCloud+ · Managed billing",
                    "features": ["Google Drive or Apple iCloud+", "Private space with isolated access", "Managed billing · 7×16h 1-on-1 support"],
                    "btn": "Subscribe 2 TB"
                },
                {
                    "badge": "Creator pick",
                    "tier_b": "6 TB",
                    "tier_span": "Storage",
                    "desc": "Ideal for photographers, creators and personal archive vaults.",
                    "note": "Google Drive or iCloud+ · Managed billing",
                    "features": ["Google Drive or Apple iCloud+", "Full-res photos and 4K media sync", "Managed billing · 7×16h 1-on-1 support"],
                    "btn": "Subscribe 6 TB"
                },
                {
                    "tier_b": "12 TB",
                    "tier_span": "Storage",
                    "desc": "High-capacity vault for power users and multi-device backups.",
                    "note": "Google Drive or iCloud+ · Managed billing",
                    "features": ["Google Drive or Apple iCloud+", "Large project archives & device mirrors", "Managed billing · 7×16h 1-on-1 support"],
                    "btn": "Subscribe 12 TB"
                },
                {
                    "tier_b": "30 TB",
                    "tier_span": "Flagship",
                    "desc": "Studio-grade cloud vault for RAW footage, AI datasets and long-term archives.",
                    "note": "Google Drive or iCloud+ · Concierge ops",
                    "features": ["Google Drive 30TB or dual-cloud combo", "High-speed global team collaboration", "Top-tier 7×24h private concierge"],
                    "btn": "Subscribe 30 TB"
                }
            ]
        },
        "stripe_trust_html": "Secure checkout by <strong>Stripe</strong> · Visa / Mastercard / Amex / UnionPay / Apple Pay / Google Pay · Monthly or annual (2 months free), cancel any time",
        "foot_before_currency": "All prices include a physical high-spec Mac environment (separate account on 1x / 5x, dedicated machine option on 20x, dedicated host or multi-Mac cluster on Team / Business), pre-configured AI toolchain, and concierge subscription & billing management, billed monthly or annually (10 months for 12) in ",
        "foot_after_currency": ". Prices in each currency reflect local market levels. ",
        "foot_promo": "The struck-through 20x price is the regular price, which applies to new subscriptions from 1 January 2027. ",
        "foot_legal_prefix": "By subscribing you agree to our ",
        "foot_terms_link": "Terms of Service",
        "foot_legal_mid": " and ",
        "foot_refund_link": "Refund Policy",
        "foot_legal_suffix": "."
    },
    "process": {
        "tag": "Process",
        "h2": "Four steps. Up and running the same day.",
        "steps": [
            {"h3": "Choose a plan", "p": "Pick 1x, 5x or 20x and your currency, or email us first."},
            {"h3": "Subscribe via Stripe", "p": "Choose your preferred region on the secure Stripe checkout and complete your monthly or annual subscription."},
            {"h3": "Delivery", "p": "The same day, we assign your high-spec Mac and separate account (dedicated machine on 20x), and send your access details and guide."},
            {"h3": "Ongoing operations", "p": "Renewals, account maintenance and troubleshooting stay with us."}
        ]
    },
    "faq": {
        "tag": "FAQ",
        "h2": "Frequently asked questions",
        "items": [
            {
                "q": "Who operates Zaokit ClaudeOps?",
                "a_html": "Zaokit ClaudeOps is operated by an Australian registered company. Payments are processed securely by Stripe, and every payment comes with an official receipt and invoice."
            },
            {
                "q": "How do 1x, 5x, 20x, Team and Business compare? Is there an annual discount?",
                "a_html": "All five tiers scale seats, hardware isolation, concierge hours and included perks — and <strong>annual billing charges only 10 months per year (2 months free) across every tier</strong>:<br>• <strong>1x Standard</strong>: Solo base allowance + Mac mini environment (separate macOS account) + <strong>7×8h</strong> 1-on-1 support;<br>• <strong>5x Pro</strong>: Solo 5× allowance + high-spec Mac mini (separate macOS account) + <strong>7×16h</strong> priority 1-on-1 support;<br>• <strong>20x Ultimate</strong>: Solo 20× allowance + high-spec Mac Studio / Mac mini (dedicated machine option) + <strong>7×24h</strong> private concierge + <strong>private RustDesk channel</strong> + <strong>6 TB cloud storage</strong>;<br>• <strong>Team (5 Seats · Dedicated Host)</strong>: Available in All-Pro (1x), All-Max (5x) or All-Ultra (20x) tiers — dedicated physical Mac host for your team, seat reassignment, consolidated billing, private RustDesk channel, 6–12 TB cloud storage &amp; 7×24h team concierge;<br>• <strong>Business (10 Seats · Multi-Mac Cluster)</strong>: Available in All-Pro (1x), All-Max (5x) or All-Ultra (20x) tiers — dedicated multi-Mac cluster (9-country dual-region deployment &amp; rapid migration), commercial invoicing, enterprise RustDesk relay, 12–30 TB cloud storage &amp; 7×24h VIP SLA;<br>• <strong>Per-Seat Upgrade Add-ons</strong>: Start on an All-Pro or All-Max base plan and upgrade specific seats to Max (5x) or Ultra (20x) at any time via self-serve checkout (adjustable quantity 1–50 seats);<br>• <strong>ClaudeOps Enterprise Dedicated Line Add-on</strong>: Optional enterprise BGP cross-border acceleration for 1x (+$5/mo) and 5x (+$20/mo) subscribers (already complimentary on 20x, Team &amp; Business)."
            },
            {
                "q": "What is the ClaudeOps Enterprise Dedicated Line add-on? Who needs it?",
                "a_html": "The <strong>ClaudeOps Enterprise Dedicated Line</strong> routes your remote desktop and terminal traffic over our premium enterprise BGP cross-border backbone with self-hosted relays and dual-leg BBR congestion control, eliminating peak-hour public internet jitter and packet loss:<br>• <strong>1x Dedicated Line ($5/mo · $50/yr)</strong>: Designed for 1x Standard solo subscribers running daily Apple Screen Sharing, SSH and light coding;<br>• <strong>5x Dedicated Line ($20/mo · $200/yr)</strong>: Designed for 5x Pro engineering workloads with 5× priority bandwidth quota and high-priority BGP QoS (20% lower unit cost vs 1x);<br>• <strong>Included Free on Flagship &amp; Team Tiers</strong>: <strong>20x Ultimate, Team and Business plans already include dedicated enterprise acceleration at no extra charge</strong>."
            },
            {
                "q": "Why is Zaokit ClaudeOps priced higher than standard cloud desktops or shared accounts?",
                "a_html": "Because you are paying for <strong>deterministic physical infrastructure and white-glove engineering operations</strong>—not low-cost shared VPS instances or pooled logins. Every subscription covers four real infrastructure costs:<br>• <strong>High-Spec Physical Mac Hardware</strong>: Real Mac Studio and Mac mini machines (never virtualized cloud VMs), delivering sustained local compute and 24/7 reliability—with full dedicated machine isolation on 20x+;<br>• <strong>200Mbps–500Mbps+ Symmetrical Native Bandwidth</strong>: Local native ISP broadband across 9 countries with generous symmetrical upload/download speeds, keeping Screen Sharing crisp and responsive instead of lagging on 10–30Mbps shared pipes;<br>• <strong>Enterprise BGP Backbone</strong>: Self-hosted high-speed relays over a premium HK/APAC enterprise BGP backbone with dual-leg BBR optimization, driving cross-border packet loss to zero;<br>• <strong>Full Official Allowance + 7×16 / 7×24 Concierge Ops</strong>: Full official subscription allowances, managed billing, iCloud/Google Drive sync, and 1-on-1 engineering support."
            },
            {
                "q": "Separate account vs dedicated machine: why is 1x / 5x limited to Apple Screen Sharing?",
                "a_html": "• <strong>Separate account isolation (1x / 5x)</strong>: several users share one high-spec Mac, but each has their own macOS account, files and permissions, and no one can see anyone else's data. To protect every user's privacy, access is limited to <strong>Apple Screen Sharing</strong>, which creates an isolated desktop session for each account so your screen and activity stay private.<br>• <strong>Dedicated machine (available on 20x)</strong>: the entire physical Mac serves only you. Hardware, system and network are fully yours. Install any software, change system-level settings and use <strong>any remote desktop tool</strong>: Apple Screen Sharing, third-party VNC such as RealVNC / TigerVNC, or our self-hosted high-speed RustDesk channel (complimentary on 20x).<br><strong>Why no third-party remote tools on shared machines?</strong> RustDesk and most third-party VNC tools capture the Mac's main screen session, which on a multi-user machine could let others see or even control your desktop. We only enable them in dedicated mode. It is a deliberate privacy safeguard."
            },
            {
                "q": "Which plan should I choose?",
                "a_html": "Choose 1x for everyday chat and writing, 5x if you code with Claude Code every day, and 20x for multiple agents, heavy round-the-clock use, or a dedicated machine with RustDesk and any remote desktop tool. Not sure? Start lower and upgrade any time."
            },
            {
                "q": "What does a \"deterministic, stable environment\" mean in practice?",
                "a_html": "It means your own isolated workspace + a fixed physical high-spec Mac workstation + dedicated billing, renewal and day-to-day engineering ops. Standardized engineering operations eliminate unexpected drops, configuration conflicts and failed renewals so your workflow stays predictable."
            },
            {
                "q": "How do I actually use it? Remote Mac or local?",
                "a_html": "<strong>Both work. Use whichever suits you:</strong><br>1. <strong>Remote desktop</strong>: on 1x / 5x, sign in to your separate account with macOS Screen Sharing, which is isolated, secure and ready to go. On 20x with dedicated mode enabled, you can also use third-party VNC such as RealVNC / TigerVNC, or our <strong>self-hosted high-speed RustDesk channel (complimentary on 20x)</strong> for smoother, lower-latency sessions. Either way you get the full macOS desktop and terminal, and long tasks keep running.<br>2. <strong>Seamless local workflow integration</strong>: collaborate with the remote development environment directly from your local workflow and dev tools, with no local environment set-up or maintenance overhead. The remote Mac becomes your dedicated compute back end."
            },
            {
                "q": "How are my code and data kept secure and private?",
                "a_html": "On 1x / 5x, every user gets a separate macOS account with isolated files, permissions and desktop sessions, accessed only via Apple Screen Sharing so no one else can see your screen. On 20x you can enable a dedicated machine: the entire high-spec Mac Studio or Mac mini serves only you, isolated right down to the hardware. Your session history, source code and environment variables stay in your own account or machine. You set your own access passwords and encryption, and our team does not actively access your data except for maintenance, security incidents or troubleshooting you authorise."
            },
            {
                "q": "Where are the machines and networks located?",
                "a_html": "Our physical high-spec Mac Studio and Mac mini machines are located in <strong>Australia, the United States, Singapore, Malaysia, Indonesia, Japan, Cambodia, New Zealand and Canada</strong>, connected via <strong>local native ISP broadband networks (not shared public cloud data centers)</strong> for maximum reliability. Pick your preferred region at checkout, and we assign you a fixed machine and account for the long term (whole machine dedicated on 20x)."
            },
            {
                "q": "How does Google Drive & iCloud+ cloud storage work?",
                "a_html": "We offer 2 TB ($8.99/mo), 6 TB ($28.99/mo), 12 TB ($58.99/mo) and 30 TB ($148.99/mo) plans. At Stripe checkout, choose <strong>Apple iCloud+</strong> or <strong>Google Drive (Google One)</strong> and note your account email; our 7×16h 1-on-1 concierge team handles activation and ongoing renewals."
            },
            {
                "q": "Can I upgrade or downgrade?",
                "a_html": "Yes. Changes apply from your next billing cycle. If you need an upgrade straight away, contact us and we will charge the difference."
            },
            {
                "q": "What if something goes wrong?",
                "a_html": "Contact us straight away. We prioritise troubleshooting and get you back up and running as fast as possible."
            },
            {
                "q": "Which payment methods do you accept? Can I get an invoice?",
                "a_html": "We accept online subscriptions via Stripe, including Visa, Mastercard, Amex, UnionPay, Apple Pay, Google Pay and Link, billed in AUD, USD, EUR, NZD, CAD, SGD or CNY. UnionPay cardholders can choose CNY for a smoother payment. Stripe issues an official receipt and invoice automatically. For multi-account business plans, email us."
            },
            {
                "q": "How can I bring my own machine or join your global compute network to earn while lighting up more cities?",
                "a_html": "We warmly invite partners around the world to join our native compute network as we work toward truly serving all 8 billion people! <strong>You can bring your own machine and share your resources — helping you earn revenue while lighting up the possibility of dreams for others!</strong> Whether you have idle or high-spec physical Mac hardware, quality local native broadband in your city, or regional builder &amp; creator community reach, email us any time at <a href=\"mailto:jason2023zhang@gmail.com?subject=Bring%20My%20Mac%20%2F%20Join%20Zaokit%20Global%20Compute%20Network\" style=\"color:var(--primary-strong);font-weight:600\">jason2023zhang@gmail.com</a> with your city and hardware/ISP details—welcome aboard!"
            }
        ]
    },
    "partner": {
        "eyebrow": "GLOBAL COMPUTE PARTNER · Co-Building the World's Compute Mesh",
        "h2_html": "Join Our Global Compute Network —<br><em class=\"grad\">Truly Serving All 8 Billion People!</em>",
        "p_html": "Starting from 13+ lit cities across 9 countries, we are bringing pure native compute and frontier AI productivity to every corner of the world. <strong>You can bring your own machine and share your resources — helping you earn revenue while lighting up the possibility of dreams for others!</strong> Wherever you are, welcome aboard — email us directly to light up the next city together.",
        "chips": [
            "✦ Bring Your Own Mac · Share & Earn",
            "✦ Local Native Broadband Resource Sharing",
            "✦ Cluster Hosting & Regional Partners"
        ],
        "btn": "Bring Your Mac / Email Us: jason2023zhang@gmail.com →"
    },
    "cta": {
        "h2": "AI Makes the World Borderless. Start Today.",
        "p": "Join builders across our lit global cities — subscribe via Stripe for same-day delivery of the most advanced AI productivity and top-tier experience.",
        "btn_primary": "Choose a plan",
        "btn_secondary": "Email: jason2023zhang@gmail.com",
        "tg_qr_aria": "Open Telegram @letcode2020",
        "tg_qr_alt": "Telegram QR code @letcode2020",
        "tg_h3": "Chat on Telegram",
        "tg_p": "Scan or tap to add us for pre-sales questions, technical support and AI insights."
    },
    "footer": {
        "brand": "Zaokit ClaudeOps",
        "entity": "Operated by an Australian registered company · 19 Global Languages",
        "contact_label": "Contact: ",
        "alt_label": "Alt: ",
        "rights": "All rights reserved.",
        "products_h4": "Zaokit products",
        "follow_h4": "Follow us",
        "terms": "Terms of Service",
        "refund": "Refund Policy",
        "privacy": "Privacy Policy",
        "disclaimer": "Disclaimer: Zaokit is an independent cloud workstation and AI engineering consultancy and is not affiliated with, endorsed by, or sponsored by Anthropic PBC, Apple Inc., or Google LLC. Claude, Claude Code, Mac, iCloud, and Google Drive are trademarks of their respective owners."
    },
    "js": {
        "per_month": "/ month",
        "per_year": "/ year",
        "per_seat_mo": "/ seat / mo",
        "per_seat_yr": "/ seat / yr",
        "per_mo_short": "/ mo",
        "per_yr_short": "/ yr",
        "title_12mo": "12 months billed monthly",
        "title_reg_mo": "Regular monthly price",
        "note_annual": "10 months billed annually · ~{sym}{eq}/mo, save {sym}{save}",
        "note_1x_mo": "Includes Claude environment · about {sym}{day} / day",
        "note_20x_promo": "Promo price stays on renewal · unit cost about {ratio}% of 1x",
        "note_mult_mo": "Includes Claude environment · {mult}x usage, unit cost about {ratio}% of 1x",
        "ent_team_mo": "Includes 5 {label} isolated seats · Dedicated Mac host & consolidated billing",
        "ent_biz_mo": "Includes 10 {label} isolated seats · Dedicated multi-Mac cluster & VIP SLA",
        "line_0_mo": "24/7 BGP zero-loss acceleration · Managed with plan",
        "line_1_mo": "5× priority throughput · High-priority BGP QoS",
        "ent_copy": {
            "pro": {
                "label": "Pro (1x)",
                "teamBadge": "5 × Pro (1x) Seats · Dedicated Host",
                "bizBadge": "Enterprise · 10 × Pro (1x) Cluster",
                "teamSeatLi": "Includes <strong>5 Pro (1x) standard member seats</strong> (separate Claude workspace &amp; macOS account per member)",
                "bizSeatLi": "Includes <strong>10 Pro (1x) standard member seats</strong> (expandable to 50+ seats on demand)",
                "teamStorage": "Complimentary 6 TB team cloud storage (Google Drive / iCloud+)",
                "bizStorage": "Complimentary 12 TB enterprise cloud storage (Google Drive / iCloud+)"
            },
            "max": {
                "label": "Max (5x)",
                "teamBadge": "5 × Max (5x) Seats · Dedicated Host",
                "bizBadge": "Enterprise · 10 × Max (5x) Cluster",
                "teamSeatLi": "Includes <strong>5 Max (5x) engineering seats</strong> (separate Claude workspace &amp; macOS account per member)",
                "bizSeatLi": "Includes <strong>10 Max (5x) engineering seats</strong> (expandable to 50+ seats on demand)",
                "teamStorage": "Complimentary 12 TB team cloud storage (Google Drive / iCloud+)",
                "bizStorage": "Complimentary 30 TB enterprise cloud storage (Google Drive / iCloud+)"
            },
            "ultra": {
                "label": "Ultra (20x)",
                "teamBadge": "5 × Ultra (20x) Seats · Dedicated Studio",
                "bizBadge": "Enterprise · 10 × Ultra (20x) Cluster",
                "teamSeatLi": "Includes <strong>5 Ultra (20x) flagship seats</strong> (separate Claude workspace &amp; macOS account per member)",
                "bizSeatLi": "Includes <strong>10 Ultra (20x) flagship seats</strong> (expandable to 50+ seats on demand)",
                "teamStorage": "Complimentary 12 TB team cloud storage (Google Drive / iCloud+)",
                "bizStorage": "Complimentary 30 TB enterprise cloud storage (Google Drive / iCloud+)"
            }
        },
        "toast_copied": "Email copied: {email}. Opening your mail app…",
        "toast_fallback": "Please email us at {email}"
    },
    "legal_common": {
        "back_home": "← Back to home",
        "footer_copy": "© Zaokit AI · Operated by an Australian registered company"
    },
    "privacy": {
        "title": "Privacy Policy | Zaokit ClaudeOps",
        "description": "Zaokit ClaudeOps Privacy Policy",
        "h1": "Privacy Policy",
        "meta": "Effective date: 3 November 2026. If versions in different languages differ, the English version prevails.",
        "lead_html": "This policy explains how we collect, use, store and protect your personal information when providing Zaokit ClaudeOps. We handle personal information in line with the Australian Privacy Act 1988 and the Australian Privacy Principles (APPs).",
        "sections": [
            {
                "h2": "1. Information we collect",
                "body_html": "<ul><li><strong>Contact and account details</strong>: your name, email address and the preferred region you choose at checkout.</li><li><strong>Payment information</strong>: processed by Stripe. We never see or store your full card number; we can only see transaction records, receipts and payment status.</li><li><strong>Service information</strong>: third-party account emails you provide to set up the Service (such as Claude, Google or Apple accounts) and the access credentials we issue to you.</li><li><strong>Communications</strong>: messages you send us by email, Telegram or other channels.</li><li><strong>Website data</strong>: device, browser, IP address and pages visited, collected through analytics tools such as Google Analytics and Umami.</li></ul>"
            },
            {
                "h2": "2. How we use it",
                "body_html": "<p>We use this information only to set up and deliver the Service, handle billing and renewals, provide support, keep our systems secure and prevent abuse, meet legal obligations, and improve our website and Service. We do not sell your personal information.</p>"
            },
            {
                "h2": "3. Data in your environment",
                "body_html": "<p>Files, code and sessions you store in your environment belong to you. We do not actively access them, and only take necessary action for system maintenance, security incidents, legal requirements or troubleshooting you have authorised.</p>"
            },
            {
                "h2": "4. Sharing",
                "body_html": "<p>We only share necessary information with:</p><ul><li>service providers we need to deliver the Service, such as payment processing (Stripe), website analytics, and network and infrastructure providers;</li><li>third-party providers, where needed to manage subscriptions on your behalf;</li><li>authorities, where required by law or a lawful government request.</li></ul>"
            },
            {
                "h2": "5. Cross-border processing",
                "body_html": "<p>Our environments are located in Australia, the United States, Singapore, Malaysia, Indonesia, Japan, Cambodia, New Zealand and Canada, and providers such as Stripe may process data in other countries. Your information may therefore be stored or processed outside your country. We take reasonable steps to protect it.</p>"
            },
            {
                "h2": "6. Retention",
                "body_html": "<ul><li>Contact, account and billing information: kept while you use the Service and afterwards for as long as tax, accounting or other laws require.</li><li>Data in your environment: may be deleted 7 days after the Service ends.</li></ul>"
            },
            {
                "h2": "7. Security",
                "body_html": "<p>We use reasonable technical and organisational measures to protect your information, such as access controls and account isolation. However, no internet transmission or storage is completely secure, and we cannot guarantee that information will never be accessed without authorisation.</p>"
            },
            {
                "h2": "8. Cookies and analytics",
                "body_html": "<p>Our website uses analytics tools to understand how it is used, and these tools may use cookies or similar technologies. You can disable cookies in your browser settings and still browse the site.</p>"
            },
            {
                "h2": "9. Your rights",
                "body_html": "<p>You can ask us to access, correct or delete your personal information, except where we must keep it by law. If you have a concern about how we handle your information, please contact us first. If we cannot resolve it, you may complain to the Office of the Australian Information Commissioner (OAIC).</p>"
            },
            {
                "h2": "10. Changes",
                "body_html": "<p>We may update this policy from time to time and will publish the updated version on this page. We will give advance notice of material changes by email or on our website.</p>"
            },
            {
                "h2": "11. Contact",
                "body_html": "<p>For privacy questions, email <a href=\"mailto:jason2023zhang@gmail.com\">jason2023zhang@gmail.com</a> (alternative: <a href=\"mailto:support@zaokit.ai\">support@zaokit.ai</a>).</p>"
            }
        ]
    },
    "terms": {
        "title": "Terms of Service | Zaokit ClaudeOps",
        "description": "Zaokit ClaudeOps Terms of Service",
        "h1": "Terms of Service",
        "meta": "Effective date: 3 November 2026. If versions in different languages differ, the English version prevails.",
        "lead_html": "Welcome to Zaokit ClaudeOps (\"we\", \"us\"). By subscribing to or using the service, you agree to these Terms, our <a href=\"refund.html\">Refund Policy</a> and our <a href=\"privacy.html\">Privacy Policy</a>. If you do not agree, please do not subscribe.",
        "sections": [
            {
                "h2": "1. The service",
                "body_html": "<p>We provide managed remote Mac environments, AI workspace configuration, subscription billing management and technical consulting (the \"Service\"). We are an independent provider and are not affiliated with, authorised by or partnered with Anthropic PBC, Apple Inc. or Google LLC.</p>"
            },
            {
                "h2": "2. Third-party services",
                "body_html": "<ol><li>Third-party services such as Claude, Google Drive and iCloud+ are provided by their respective providers under their own terms and policies. These accounts are registered in your name and belong to you. You are responsible for complying with each provider's terms, usage policies and regional requirements, and for making sure your use is lawful where you are.</li><li>We only manage subscriptions and renewals on your behalf. We make no guarantee about the availability, features, usage limits, model versions or policy changes of any third-party service. The \"1x / 5x / 20x\" plan multipliers and Team / Business seat configurations are indicative specifications only. Actual usage is subject to the provider's rules at the time.</li><li>If a third-party provider restricts, suspends or terminates your account, or changes its products, limits or prices, we will make reasonable efforts to help, but we are not liable for the impact.</li></ol>"
            },
            {
                "h2": "3. Environments",
                "body_html": "<ol><li><strong>1x / 5x (multi-user machines)</strong>: each user has a separate macOS account, accessible only via Apple Screen Sharing. You must not attempt to access other users' accounts or data, or install remote control, screen recording, network proxy or other software that may affect other users.</li><li><strong>20x / Team / Business (dedicated machine or cluster)</strong>: 20x includes a dedicated machine option; Team and Business plans provide dedicated physical hardware or multi-Mac clusters exclusively for your organisation, with a separate macOS account per member. You may install software and change system settings within reason, and you are responsible for any resulting stability or security issues.</li><li>Machine model, specification and region are allocated based on available resources. We will try to honour the preferred region you select at checkout but cannot guarantee it. We may migrate your environment for maintenance, incident handling or capacity reasons, and will try to give notice in advance except in emergencies.</li></ol>"
            },
            {
                "h2": "4. Acceptable use",
                "body_html": "<p>You must not use the Service to:</p><ul><li>engage in unlawful activity or infringe the intellectual property, privacy or other rights of others;</li><li>send spam, launch attacks, run port scans or distribute malware;</li><li>mine cryptocurrency or run sustained high-load computing unrelated to the Service;</li><li>resell or sublet the Service, or share your access credentials with others;</li><li>breach any third-party provider's terms or usage policies.</li></ul><p>If you breach these rules, we may suspend or terminate the Service immediately without refund.</p>"
            },
            {
                "h2": "5. Support",
                "body_html": "<p>The support hours shown for each plan (7×8h / 7×16h / 7×24h) describe when we accept and handle requests. We will make reasonable efforts to respond promptly but do not commit to specific response or resolution times.</p>"
            },
            {
                "h2": "6. Availability and maintenance",
                "body_html": "<p>The Service is provided on an \"as is\" and \"as available\" basis. We make reasonable efforts to keep it stable but do not guarantee it will be uninterrupted or error-free. We will try to give advance notice of planned maintenance. Interruptions caused by power outages, network carrier faults, third-party outages, natural disasters or other events beyond our reasonable control are not a breach by us.</p>"
            },
            {
                "h2": "7. Data and backups",
                "body_html": "<ol><li>You are responsible for the data in your account and should back up important data regularly. We are not liable for data loss except where required by law.</li><li>We do not actively access content in your account, and only take necessary action for system maintenance, security incidents, legal requirements or troubleshooting you have authorised.</li><li>After the Service ends, we may delete your account and data after 7 days. Please export anything you need before then.</li></ol>"
            },
            {
                "h2": "8. Fees and renewals",
                "body_html": "<ol><li>The Service may be billed monthly or annually and renews automatically via Stripe at the price and billing interval shown at checkout. Per-seat upgrade add-ons apply only to active Team or Business base subscriptions; ClaudeOps Enterprise Dedicated Line add-ons require an active base subscription (included at no extra charge on 20x, Team and Business plans).</li><li>We may change prices with at least 30 days' notice. You may cancel before the new price takes effect.</li><li>Promotional prices apply only to subscriptions started during the promotion period. While your subscription remains continuously active, renewals are charged at the promotional price, subject to clause 8.2. If you cancel and later resubscribe, the then-current price applies.</li><li>Cancellation and refunds are covered by our <a href=\"refund.html\">Refund Policy</a>.</li></ol>"
            },
            {
                "h2": "9. Suspension and termination",
                "body_html": "<p>You may cancel at any time and the Service continues until the end of the current billing period. We may suspend or terminate the Service if you breach these Terms, fail to pay, or your use creates a security risk. We may also discontinue the Service with 30 days' notice and refund, on a pro-rata basis, any fees paid for the unused period.</p>"
            },
            {
                "h2": "10. Limitation of liability",
                "body_html": "<p>To the maximum extent permitted by law: (a) we are not liable for any indirect, incidental, special or consequential loss, including loss of profit, data, goodwill or business; and (b) our total liability in connection with the Service is limited to the fees you actually paid us in the one month before the event giving rise to the claim.</p><p>Nothing in these Terms excludes, restricts or modifies any right or guarantee you have under the Australian Consumer Law that cannot lawfully be excluded. Where the law allows us to limit our liability, our liability is limited to supplying the services again or paying the cost of having them supplied again.</p>"
            },
            {
                "h2": "11. Changes to these Terms",
                "body_html": "<p>We may update these Terms from time to time and will give advance notice of material changes by email or on our website. Continuing to use the Service after changes take effect means you accept the updated Terms.</p>"
            },
            {
                "h2": "12. Governing law",
                "body_html": "<p>These Terms are governed by the laws of Australia.</p>"
            },
            {
                "h2": "13. Contact",
                "body_html": "<p>Questions about these Terms? Email <a href=\"mailto:jason2023zhang@gmail.com\">jason2023zhang@gmail.com</a> (alternative: <a href=\"mailto:support@zaokit.ai\">support@zaokit.ai</a>).</p>"
            }
        ]
    },
    "refund": {
        "title": "Refund Policy | Zaokit ClaudeOps",
        "description": "Zaokit ClaudeOps Refund and Cancellation Policy",
        "h1": "Refund Policy",
        "meta": "Effective date: 3 November 2026. If versions in different languages differ, the English version prevails.",
        "lead_html": "This policy sets out how cancellations and refunds work and forms part of our <a href=\"terms.html\">Terms of Service</a>. It does not exclude any rights you have under the Australian Consumer Law that cannot lawfully be excluded.",
        "sections": [
            {
                "h2": "1. Cancelling",
                "body_html": "<p>The Service may be billed monthly or annually and you can cancel at any time. After you cancel, the Service continues until the end of the current billing period (monthly or annual) and will not renew. To cancel, email us.</p>"
            },
            {
                "h2": "2. Before delivery",
                "body_html": "<p>If you cancel before we deliver your environment and access details, we will give you a full refund.</p>"
            },
            {
                "h2": "3. After delivery",
                "body_html": "<p>When we activate the Service, we allocate hardware and seat resources and arrange the related third-party subscriptions on your behalf. For this reason, fees for the current billing period (including discounted annual prepayments) are generally not refundable after delivery and are not pro-rated by day or month, except as set out in section 4 or where required by law.</p>"
            },
            {
                "h2": "4. Outages caused by us",
                "body_html": "<p>If the Service is unavailable for more than 72 consecutive hours for reasons within our control, we will extend your service period by the number of days affected. If you would rather cancel, you may request a pro-rata refund for the unused part of the current period.</p>"
            },
            {
                "h2": "5. Impact caused by third parties",
                "body_html": "<p>Impact caused by third-party providers (including Anthropic, Google and Apple), such as policy changes, usage limits, account restrictions or outages, is not within our control, and third-party fees already paid on your behalf are not refundable. We will make reasonable efforts to help you resolve the issue.</p>"
            },
            {
                "h2": "6. Cloud storage & Enterprise Dedicated Line add-ons",
                "body_html": "<p>Once cloud storage or a ClaudeOps Enterprise Dedicated Line add-on has been activated, fees for the current period are not refundable. After cancellation, the add-on continues until the end of the current period.</p>"
            },
            {
                "h2": "7. Termination for breach",
                "body_html": "<p>No refund is given if the Service is suspended or terminated because you breached our <a href=\"terms.html\">Terms of Service</a>.</p>"
            },
            {
                "h2": "8. How to request a refund",
                "body_html": "<ol><li>Email <a href=\"mailto:jason2023zhang@gmail.com\">jason2023zhang@gmail.com</a> with your subscription email, Stripe receipt number and the reason for your request.</li><li>We will reply within 5 business days.</li><li>Approved refunds are returned to your original payment method. Processing time depends on your bank or payment provider.</li></ol>"
            },
            {
                "h2": "9. Chargebacks",
                "body_html": "<p>If you have a question about a charge, please contact us first and we will sort it out quickly. If you file a chargeback with your bank without contacting us, we may suspend the related service while the dispute is open.</p>"
            }
        ]
    }
}


ZH_LOCALE = {
    "meta": {
        "title": "Claude 代运营 · Zaokit ClaudeOps — AI 让世界无界，为所有人带来最先进的生产力，最 TOP 的体验",
        "description": "Zaokit ClaudeOps：AI 让世界无界，点亮世界每一个城市，我们要为所有人带来最先进的生产力、最 TOP 的体验。提供独立专属工作空间、高配置 Mac Studio 与 Mac mini 物理环境（澳大利亚、美国、新加坡、马来西亚、印尼、日本、柬埔寨、新西兰、加拿大 9 国本地原生宽带算力节点）、企业精品跨境专线、最高 7×24 小时一对一工程顾问及 2TB–30TB 云存储全托管。",
        "keywords": "Claude 代运营, Zaokit ClaudeOps, AI 让世界无界, 点亮世界每一个城市, Claude 工作空间托管, Claude Code, Mac 云工作站, AI 工程顾问",
        "og_title": "AI 让世界无界 — 为所有人带来最先进的生产力，最 TOP 的体验 | Zaokit ClaudeOps",
        "og_description": "点亮世界每一个城市 · 全球 9 国原生算力网络 · 高配物理 Mac 工作站 · 企业精品跨境专线 · 最高 7×24h 一对一工程顾问全托管。",
        "ld_description": "AI 让世界无界，点亮世界每一个城市，为所有人带来最先进的生产力与最 TOP 的体验：独立专属工作空间、全球 9 国原生宽带高配 Mac 物理环境、企业精品跨境专线及最高 7×24h 一对一工程顾问全托管服务。",
        "offer_names": ["1x 标准版", "5x 专业版", "20x 旗舰版"]
    },
    "nav": {
        "brand": "Claude 代运营",
        "why": "为什么需要",
        "service": "服务内容",
        "value": "不止算力",
        "security": "安全与隐私",
        "reviews": "用户评价",
        "pricing": "价格方案",
        "storage": "云存储",
        "process": "开通流程",
        "faq": "常见问题",
        "lang_aria": "切换语言"
    },
    "hero": {
        "eyebrow": "GLOBAL VISION · 让 AI 点亮世界每一个城市，每一个个体",
        "h1_main": "AI 让世界无界",
        "h1_sub": "我们要为所有人带来最先进的生产力，最 TOP 的体验",
        "lead": "我们相信，最前沿的 AI 生产力不应只是少数人的特权。从悉尼、硅谷、东京、新加坡到雅加达——我们正在全球一座座城市点亮纯净原生算力节点，以隔离稳定的物理 Mac 工作站、企业精品跨境专线与最高 7×24 小时一对一工程顾问，抹平地域、网络与技术门槛，让每一位创造者、开发者与团队都能无界拥有确定性的 AI 创造力。",
        "cta_primary": "查看价格方案",
        "cta_secondary": "邮件咨询",
        "mailto_enquiry_subject": "Claude 代运营咨询",
        "stats": [
            {"strong": "点亮 9 国城市", "span": "澳·美·新·马·印尼·日·柬·新西兰·加"},
            {"strong": "物理 Mac 算力", "span": "高配 Mac Studio / Mac mini"},
            {"strong": "最 TOP 体验", "span": "7×8h / 7×16h / 7×24h 1对1顾问"},
            {"strong": "专属安全空间", "span": "独立账户隔离 · 20x/团队整机独享"},
            {"strong": "澳洲注册公司", "span": "合规企业主体 · Stripe 全球结算"}
        ]
    },
    "map": {
        "status_main": "点亮世界每一个城市 · 已点亮 9 国 13+ 核心城市节点",
        "status_em": "LIGHTING UP EVERY CITY",
        "meta_1": "本地原生宽带算力网",
        "meta_2": "精品 BGP 无界互联",
        "meta_3": "悬停或点击城市节点",
        "stage_aria": "9 国本地原生宽带算力网络全球拓扑图",
        "hud_live": "● 在线运行",
        "hud_label_city": "核心城市",
        "hud_label_hw": "物理硬件",
        "hud_val_hw": "Mac Studio / 高配 mini",
        "hud_label_route": "骨干路由",
        "pills_aria": "切换 9 国节点",
        "partner_pill": "✦ 全球算力共创 · 服务全球 80 亿人",
        "partner_copy_html": "<strong>您可以带机加入，共享您的资源。帮助您赚钱的同时，为别人点亮梦想的可能！</strong>欢迎全球伙伴加入！",
        "partner_cta": "发邮件带机/合作加入 →",
        "partner_mailto_subject": "带机加入 Zaokit 全球算力网络 - 共享资源点亮城市",
        "partner_mailto_body": "您好，我希望加入 Zaokit 全球算力网络，共享资源、共同点亮更多城市：\n\n1. 所在国家 / 城市：\n2. 合作方式（带机加入共享 Mac 算力 / 本地原生宽带节点 / 区域生态伙伴）：\n3. 设备与网络简况（如带机加入可简述 Mac 型号与宽带运营商）：\n4. 联系方式：",
        "nodes": {
            "AU": {"name": "澳大利亚", "pill": "澳大利亚 ★", "short": "澳大利亚", "city": "悉尼 · 墨尔本", "role": "★ 澳洲注册主体 · 首选主力节点", "route": "香港精品 BGP 骨干直达 · 0% 丢包"},
            "US": {"name": "美国", "pill": "美国", "short": "美国", "city": "硅谷 · 洛杉矶", "role": "北美西海岸核心算力节点", "route": "跨太平洋直连骨干 · 原生宽带 ISP"},
            "SG": {"name": "新加坡", "pill": "新加坡", "short": "新加坡", "city": "新加坡", "role": "亚太低延迟核心交换枢纽", "route": "亚太海缆核心交汇 · 极速直连"},
            "MY": {"name": "马来西亚", "pill": "马来西亚", "short": "马来西亚", "city": "吉隆坡", "role": "东南亚原生家庭宽带节点", "route": "新马高速陆缆互联 · 纯净原生网络"},
            "ID": {"name": "印度尼西亚", "pill": "印度尼西亚", "short": "印尼", "city": "雅加达", "role": "东南亚核心群岛原生宽带节点", "route": "新印 & 印澳海缆双路由直连"},
            "JP": {"name": "日本", "pill": "日本", "short": "日本", "city": "东京 · 大阪", "role": "东亚超低延迟旗舰节点", "route": "实测 ~92ms · 0% 丢包跟手直连"},
            "KH": {"name": "柬埔寨", "pill": "柬埔寨", "short": "柬埔寨", "city": "金边", "role": "东南亚陆缆直连低延迟节点", "route": "实测 ~81ms 陆缆直连 · 0% 丢包"},
            "NZ": {"name": "新西兰", "pill": "新西兰", "short": "新西兰", "city": "奥克兰", "role": "南太平洋高纯净度原生节点", "route": "跨塔斯曼 & 跨太平洋双海缆接入"},
            "CA": {"name": "加拿大", "pill": "加拿大", "short": "加拿大", "city": "温哥华 · 多伦多", "role": "北美高纯净度原生宽带节点", "route": "环北太平洋海缆直达 · 长期稳定"}
        }
    },
    "why": {
        "tag": "Why",
        "h2": "用好 Claude，难的从来不是模型本身",
        "sub": "真正消耗精力的，是那些与创造无关的“不确定性”。",
        "cards": [
            {"h3": "配置门槛太高", "p": "从工作空间初始化到运行环境部署，每一步都要自己摸索，出了问题无人兜底。"},
            {"h3": "运行不够稳定", "p": "本地环境各不相同，Claude Code 长任务跑到一半中断时有发生。"},
            {"h3": "支付续费麻烦", "p": "订阅扣款失败、套餐升级、到期续费，每个月都要花时间处理。"},
            {"h3": "时间被反复消耗", "p": "研究工具、排查问题的时间，本该用在真正的业务和创作上。"}
        ]
    },
    "service": {
        "tag": "Service",
        "h2": "把不确定性交给我们，把确定性留给您",
        "sub": "从环境搭建到日常运维，一站式托管，开箱即用。",
        "cards": [
            {"h3": "独立专属工作空间", "p": "每位用户拥有独立 macOS 账户与专属工作空间配置，文件与权限相互隔离，20x 可开启整机独享，对话上下文与工程数据完整可控。"},
            {"h3": "高配 Mac Studio / Mac mini", "p": "专属高配置 Mac Studio 与高配置 Mac mini 物理实例，部署于澳大利亚、美国、新加坡、马来西亚、印尼、日本、柬埔寨、新西兰、加拿大 9 国本地原生宽带网络环境（非公共云共享机房），账户级隔离（20x 可整机独享）、长期纯净稳定。"},
            {"h3": "续费运维托管", "p": "订阅支付、到期续费、套餐升降级全部由我们处理，您无需操心。"},
            {"h3": "分级一对一专属支持", "p": "按方案提供 7×8h（1x）、7×16h（5x）至最高 7×24h 全天候私人顾问一对一响应（20x）。"}
        ]
    },
    "value": {
        "tag": "Beyond Compute",
        "h2_html": "您获得的，<em class=\"grad\">不止是算力</em>",
        "sub": "账号和机器只是起点。真正拉开差距的，是有人帮您把 AI 用对、用深、用在前面。",
        "cards": [
            {"h3": "顶级算力与工作站", "p": "为您配置与托管专属的高阶 AI 开发工作空间，运行在高配置 Mac Studio 与高配置 Mac mini 物理环境上，Claude Code 长任务稳定不中断。"},
            {"h3": "TOP 级一对一顾问服务", "p": "让每一位创作者、开发者与团队都能拥有专属 AI 工程顾问。不只是排障，从 Claude Code 工作流搭建、MCP 与 Skills 配置到真实项目落地，提供 7×8h / 7×16h / 7×24h 分级一对一在线指导，交付最 TOP 的体验。"},
            {"h3": "一手 AI 资讯", "p": "持续分享 Claude 与主流 AI 工具的新功能、最佳实践和行业动态，帮您第一时间用上新能力，少走弯路。"}
        ]
    },
    "network": {
        "tag": "Network",
        "h2_html": "持续投入网络优化，<br>只为跟手的远程体验",
        "p": "我们持续投入硬件与线路成本，接入上下行对等 200Mbps–500Mbps+ 的 9 国本地原生宽带，并自建高速中继与企业精品 BGP 跨境骨干，把远程桌面最怕的丢包压到 0。",
        "chips": ["上下对等 200–500Mbps+", "企业精品 BGP 骨干", "自建高速中继", "双段 BBR 抗丢包", "Apple Silicon 硬件编码", "白名单安全加固"],
        "addon_note_prefix": "20x 旗舰版及团队/企业方案已免费赠送专线；1x / 5x 用户可按需加购 ",
        "addon_note_link": "ClaudeOps 企业专线（$5 / 月起）↓",
        "addon_note_suffix": "",
        "card_aria": "网络优化前后实测对比",
        "legend_before": "优化前",
        "legend_after": "优化后",
        "rows": [
            {"country": "日本", "via": "香港骨干接力", "before": "128–184ms · 丢包 10%", "after": "~92ms · 丢包 0%"},
            {"country": "澳大利亚", "via": "香港骨干接力", "before": "343–386ms · 丢包 25–33%", "after": "~240ms · 丢包 0%"},
            {"country": "柬埔寨", "via": "陆缆直连", "before": "", "after": "~81ms · 丢包 0%"}
        ],
        "foot": "2026 年 11 月东亚客户端实测，实际体验因您所在网络而异。"
    },
    "security": {
        "tag": "Security & Privacy",
        "h2": "两级隔离架构：账户级隔离与整机独享",
        "sub": "在前沿工程开发中，终端里流转的不单是文字，更是私有仓库源码、环境变量中的敏感 API Key、内部数据库配置与业务代码。Zaokit ClaudeOps 采用两级隔离标准：1x / 5x 为每位用户分配独立的 macOS 账户，并统一通过 Apple 原生屏幕共享访问；20x 可开启整机独享，从硬件边界彻底隔离。",
        "cards": [
            {"h3": "20x 整机独享：硬件级隔离", "p": "开启整机独享后，整台高配置 Mac Studio 或 Mac mini 只为您一人服务，系统、硬件与网络完全专属。可自由安装任意软件、调整系统级配置，并使用 RustDesk、第三方 VNC 等任意远程桌面方式。"},
            {"h3": "1x / 5x 独立账户隔离", "p": "每位用户拥有独立的 macOS 账户、文件目录与权限，上下文缓存、交互历史与工程文件互不可见。访问统一使用 Apple 原生屏幕共享，每个账户拥有相互隔离的独立桌面会话，屏幕与操作不会被他人看到。"},
            {"h3": "全自主加密与密钥管理控制权", "p": "支持用户端自主设置访问密钥与配置高强度本地加密策略。运维团队仅负责底层连通性监测与续费托管，不会主动访问您账户内的数据，仅在系统维护、安全事件处置或经您授权排障时进行必要操作。"}
        ]
    },
    "reviews": {
        "tag": "Testimonials",
        "h2": "来自真实订阅用户的声音",
        "sub": "为保护客户隐私，以下展示均使用卡通头像并做匿名脱敏处理，仅保留真实使用反馈与订阅档位。",
        "badge": "已匿名 · 真实用户",
        "stars_aria": "5 分评价",
        "items": [
            {
                "name": "M***",
                "role": "跨境 AI 产品负责人",
                "quote": "“企业隧道真是清晰流畅，比我本地 ToDesk 还清晰！写代码、切窗口几乎感觉不到延迟，好用、速度快，虽然不便宜但绝对物超所值，妥妥顶级体验。”",
                "source": "来自某聊天软件",
                "plan": "5x 专业版"
            },
            {
                "name": "晨*",
                "role": "资深全栈工程师",
                "quote": "“之前本地折腾网络环境总是半路断线，接入 ClaudeOps 1x 标准版后，独立环境加上 Claude Code 全天候在线，感觉「天才程序员又复活了」😂。现在每天只管专心推需求，账单和网络完全不用操心。”",
                "source": "来自某聊天软件",
                "plan": "1x 标准版"
            },
            {
                "name": "Kyle W.",
                "role": "量化研发主管",
                "quote": "“最看重 9 国原生宽带与硬件级隔离——私有策略代码和 API Key 全跑在专属 Mac Studio 上，比自己折腾云服务器省心太多，连续跑了几个月零异常、零中断。”",
                "source": "澳洲主力节点 · 已匿名",
                "plan": "20x 旗舰版"
            },
            {
                "name": "L***",
                "role": "独立开发者",
                "quote": "“当天 Stripe 银联付款当天就交付了独立 macOS 账户，Claude Code 和常用开发工具链都预装好了。不想在环境配置和跨区支付上浪费时间的话，直接上车效率拉满。”",
                "source": "日本东京节点 · 已匿名",
                "plan": "1x 标准版"
            },
            {
                "name": "Sarah C.",
                "role": "管理咨询合伙人",
                "quote": "“我不懂运维也不想折腾命令行，7×16 小时一对一支持非常省心。配合托管的 Google Drive 同步项目文档，出差在任何设备上连上去就能接着干活。”",
                "source": "新加坡节点 · 已匿名",
                "plan": "5x 专业版"
            },
            {
                "name": "A***",
                "role": "出海电商技术总监",
                "quote": "“团队核心研发都在用，晚上挂着多 Agent 自动跑重构和测试，第二天早上直接看 PR。原生屏幕共享画质极清，Telegram 找 Jason 响应也几乎秒回。”",
                "source": "来自 Telegram 真实反馈",
                "plan": "20x 旗舰版"
            }
        ],
        "note": "* 为严格保护客户隐私与数据安全，页面评价均采用卡通头像及匿名/脱敏署名展示。"
    },
    "pricing": {
        "tag": "Pricing",
        "h2": "全系弹性方案，按需选择",
        "sub_html": "覆盖个人创作至企业多机集群，可随时升级；<strong>按年付费仅收 10 个月费用（立省 2 个月）</strong>。",
        "jump_line": "企业专线增值包 ↓",
        "jump_ent": "查看 Team / Business 方案 ↓",
        "billing_aria": "选择计费周期",
        "billing_month": "按月付费",
        "billing_year": "按年付费",
        "billing_save_badge": "免 2 个月",
        "currency_aria": "选择币种",
        "currencies": {
            "AUD": {"btn": "A$ 澳元", "name": "澳元"},
            "USD": {"btn": "$ 美元", "name": "美元"},
            "EUR": {"btn": "€ 欧元", "name": "欧元"},
            "NZD": {"btn": "NZ$ 新西兰元", "name": "新西兰元"},
            "CAD": {"btn": "C$ 加元", "name": "加元"},
            "SGD": {"btn": "S$ 新加坡元", "name": "新加坡元"},
            "CNY": {"btn": "¥ 人民币", "name": "人民币"}
        },
        "solo_subscribe": "立即订阅",
        "solo_consult": "有疑问？发送邮件咨询 →",
        "solo": [
            {
                "tier_b": "1x",
                "tier_span": "标准版",
                "desc": "适合个人日常对话、写作与轻量编程，体验 Claude 的稳定使用。",
                "init_note": "含 Claude 运行环境 · 约 A$5 / 天",
                "features_html": [
                    "基础用量额度",
                    "独立专属工作空间配置",
                    "Mac mini 物理环境",
                    "订阅账单与环境运维全托管",
                    "支持 Claude Code",
                    "<strong>7×8 小时</strong>一对一专属支持",
                    "独立 macOS 账户隔离 · Apple 屏幕共享访问"
                ],
                "mailto_subject": "Claude 代运营咨询 - 1x 标准版"
            },
            {
                "badge": "最受欢迎",
                "tier_b": "5x",
                "tier_span": "专业版",
                "desc": "适合开发者与内容创作者，Claude Code 重度日常使用的主力选择。",
                "init_note": "含 Claude 运行环境 · 5 倍额度，单位成本约为 1x 的 78%",
                "features_html": [
                    "5 倍于标准版的用量额度",
                    "独立专属工作空间配置",
                    "高配置 Mac mini 物理环境",
                    "订阅账单与环境运维全托管",
                    "Claude Code 长时间任务更从容",
                    "<strong>7×16 小时</strong>一对一优先技术支持",
                    "独立 macOS 账户隔离 · Apple 屏幕共享访问"
                ],
                "mailto_subject": "Claude 代运营咨询 - 5x 专业版"
            },
            {
                "badge_promo": "限时特惠 · 截至 2026.12.31",
                "tier_b": "20x",
                "tier_span": "旗舰版",
                "desc": "适合重度创造者、创始人及多 Agent 全天候高强度并行的单人顶配方案。",
                "orig_title": "常规价",
                "init_note": "活动期内订阅，续费延续特惠价 · 单位成本约为 1x 的 35%",
                "features_html": [
                    "20 倍于标准版的用量额度",
                    "独立专属工作空间配置",
                    "高配置 Mac Studio / Mac mini · 可开启整机独享",
                    "订阅账单与环境运维全托管",
                    "多 Agent / 多任务并行无压力",
                    "<strong>TOP 级 7×24 小时</strong>私人顾问一对一通道",
                    "免费赠送自建高速 RustDesk 专属通道",
                    "免费赠送 Google Drive 6 TB 云存储权益"
                ],
                "mailto_subject": "Claude 代运营咨询 - 20x 旗舰版"
            }
        ],
        "dedicated_line": {
            "h3_main": "ClaudeOps 企业专线 · 跨境加速增值服务",
            "h3_pill": "20x / Team / Business 已免费赠送",
            "sub": "面向 1x / 5x 订阅用户按需选配：接入企业精品 BGP 跨境骨干与双段 BBR 0% 丢包加密直连通道，消除晚高峰公网抖动，让远程屏幕共享与 Claude Code 丝滑跟手（同步享按年付费免 2 个月）。",
            "cards": [
                {
                    "code": "1x 企业专线",
                    "span": "标准加速包 · 适配 1x 标准版",
                    "desc": "接入企业精品 BGP 跨境加速骨干 + 自建低延迟加密中继 + 双段 BBR 抗丢包优化，保障单席日常远程屏幕共享（Screen Sharing）、SSH 终端与轻量 Claude Code 晚高峰 0% 丢包稳定直连。",
                    "init_note": "全天候 BGP 抗丢包直连 · 随主套餐托管",
                    "btn": "开通 1x 专线 →"
                },
                {
                    "code": "5x 企业专线",
                    "span": "专业加速包 · 适配 5x 专业版（单价立省 20%）",
                    "desc": "提供 5 倍高并发带宽吞吐配额 + 企业精品 BGP 跨境骨干高优先级 QoS 队列 + 双段 BBR 0% 丢包保障，专为 Claude Code 高频实时编码、大型代码库高频拉取与高帧率低延迟远程桌面打造。",
                    "init_note": "5 倍优先带宽吞吐 · 高优先级 QoS 队列",
                    "btn": "开通 5x 专线 →"
                }
            ]
        },
        "enterprise": {
            "divider": "Team & Business · 团队与企业专属物理集群方案",
            "switch_aria": "选择团队席位规格",
            "tier_pro": "全员 Pro 标准版 (1x)",
            "tier_max": "全员 Max 研发版 (5x)",
            "tier_max_badge": "主力推荐",
            "tier_ultra": "全员 Ultra 旗舰版 (20x)",
            "toolbar_html": "支持全员统一规格；如需定制混搭（如主创用 Ultra、研发用 Max、运营用 Pro），可先订低档底座再通过下方<strong>单席位升配包</strong>按需升级。",
            "team": {
                "init_badge": "含 5 席 Max (5x) · 团队整机独享",
                "sub": "团队版 · 5 席位",
                "desc": "专为初创核心团队、AI 工作室与投研开发小组打造，整台高配物理 Mac 团队独享，统一账单与资产归属管理。",
                "init_note": "含 5 个 Max (5x) 独立席位 · 整机物理独享 + 团队专属运维",
                "init_seat_li_html": "包含 <strong>5 个 Max (5x) 专业研发席位</strong>（每人独立 Claude 空间与 macOS 账户）",
                "features_html": [
                    "<strong>高配置 Mac Studio / Mac mini 整机团队独享</strong>，硬件级安全隔离",
                    "公司持有席位调配权，支持成员入离职交接与<strong>统一团队账单发票托管</strong>",
                    "支持后期随时按单席位补差价升配至更高额度（Max / Ultra）",
                    "<strong>7×24 小时</strong>专属团队技术顾问群一对多实时支持",
                    "免费赠送团队自建高速 RustDesk 加密专属通道"
                ],
                "init_storage_li": "免费赠送 12 TB 团队云存储权益（Google Drive / iCloud+）",
                "btn": "立即订阅 Team 版",
                "consult": "需增购额外席位或定制配置？联系团队顾问 →",
                "mailto_subject": "Claude 代运营咨询 - Team 团队版"
            },
            "biz": {
                "init_badge": "企业旗舰 · 10 席 Max (5x) 多机集群",
                "sub": "企业版 · 10 席位",
                "desc": "面向高速成长的科技企业、量化投研与跨境研发部门，多台物理 Mac 专属集群独享与 9 国跨区双节点保障。",
                "init_note": "含 10 个 Max (5x) 独立席位 · 多机物理集群独享 + VIP 专属群",
                "init_seat_li_html": "包含 <strong>10 个 Max (5x) 专业研发席位</strong>（支持按需弹性扩容至 50+ 席位）",
                "features_html": [
                    "<strong>多台高配置 Mac Studio / Mac mini 专属物理集群独享</strong>",
                    "支持 <strong>9 国双区域混合部署与故障快速迁移</strong> + 独享纯净原生静态商宽",
                    "统一商业形式发票（Commercial Invoice）、对公报销凭证与专属客户经理",
                    "<strong>TOP 级 7×24 小时企业 VIP 专属群</strong>（优先排障与架构顾问）",
                    "免费赠送企业级自建高速 RustDesk 独立中继专线"
                ],
                "init_storage_li": "免费赠送 30 TB 企业级云存储权益（Google Drive / iCloud+）",
                "btn": "立即订阅 Business 版",
                "consult": "20+ 席位或私有化专属集群？联系企业顾问 →",
                "mailto_subject": "Claude 代运营咨询 - Business 企业版"
            }
        },
        "seat_addons": {
            "h3_main": "单席位弹性升配包",
            "h3_pill": "支持 1–50 席自选数量",
            "sub": "已订阅 Team / Business 底座的团队，可随时为指定成员自助下单补差价升级额度（跟随上方月付/年付周期同步享年付免 2 个月优惠）。",
            "cards": [
                {
                    "from": "Pro 1x",
                    "to": "Max 5x",
                    "tag": "席位升配",
                    "desc": "将团队内任意 1x 标准席位升级为 5x 专业研发席位，满足日常重度 Claude Code 开发。",
                    "btn": "下单升配 →"
                },
                {
                    "from": "Max 5x",
                    "to": "Ultra 20x",
                    "tag": "席位升配",
                    "desc": "在全员 Max 研发底座上，为创始人、CTO 或核心架构师升级至 20x 顶配多 Agent 额度。",
                    "btn": "下单升配 →"
                },
                {
                    "from": "Pro 1x",
                    "to": "Ultra 20x",
                    "tag": "跨级升配",
                    "desc": "在全员 Pro 办公底座上，将指定核心技术负责人的席位一步到位直接升配至 20x 顶配额度。",
                    "btn": "下单升配 →"
                }
            ]
        },
        "storage": {
            "tag": "Cloud Storage · Google Drive & iCloud+",
            "h2": "全场景数字资产 · 云存储托管方案",
            "sub_html": "支持 <strong>Google Drive (Google One)</strong> 与 <strong>Apple iCloud+</strong>，提供 2 TB 至 30 TB 全档位配置与账单托管。独立空间权限、跨设备自动同步备份、续费全托管，享同等 7×16 小时一对一专属服务。",
            "currency_aria": "选择币种（云存储）",
            "per_mo": "/ 月",
            "cards": [
                {
                    "tier_b": "2 TB",
                    "tier_span": "云存储",
                    "desc": "充足的储存空间，适合日常照片、视频与跨设备自动备份。",
                    "note": "Google Drive / iCloud+ 任选 · 续费全托管",
                    "features": ["可选 Google Drive 或 iCloud+", "独立权限与隐私空间隔离", "续费托管 · 7×16h 一对一支持"],
                    "btn": "订阅 2 TB"
                },
                {
                    "badge": "创作者首选",
                    "tier_b": "6 TB",
                    "tier_span": "云存储",
                    "desc": "摄影师、内容创作者与个人核心数字资产长期归档的理想方案。",
                    "note": "Google Drive / iCloud+ 任选 · 续费全托管",
                    "features": ["可选 Google Drive 或 iCloud+", "海量原画照片与 4K 素材同步", "续费托管 · 7×16h 一对一支持"],
                    "btn": "订阅 6 TB"
                },
                {
                    "tier_b": "12 TB",
                    "tier_span": "云存储",
                    "desc": "为重度专业用户与多设备全量备份准备的大容量方案。",
                    "note": "Google Drive / iCloud+ 任选 · 续费全托管",
                    "features": ["可选 Google Drive 或 iCloud+", "大型工程文件与多终端镜像", "续费托管 · 7×16h 一对一支持"],
                    "btn": "订阅 12 TB"
                },
                {
                    "tier_b": "30 TB",
                    "tier_span": "旗舰存储",
                    "desc": "面向工作室、RAW 影视母带与 AI 数据集的殿堂级云端仓库。",
                    "note": "Google Drive / iCloud+ 任选 · 专人托管",
                    "features": ["Google Drive 30TB 或双端组合", "跨国团队高速协同与长久归档", "TOP 级 7×24h 私人顾问通道"],
                    "btn": "订阅 30 TB"
                }
            ]
        },
        "stripe_trust_html": "由 <strong>Stripe</strong> 提供安全加密结算 · 支持 Visa / Mastercard / Amex / 银联 UnionPay / Apple Pay / Google Pay · 按月或按年（付 10 个月享全年）均可随时取消",
        "foot_before_currency": "以上价格均含高配置 Mac 物理运行环境（1x / 5x 独立账户隔离，20x 可整机独享，Team / Business 为团队整机或多机专属集群独享）、AI 工具链预装调优及专属订阅账单托管服务，以",
        "foot_after_currency": "计，支持按月或按年订阅（年付仅收 10 个月费用），各币种价格参考当地消费水平制定。",
        "foot_promo": "20x 旗舰版划线价为常规价，2027 年 1 月 1 日起新订阅恢复常规价。",
        "foot_legal_prefix": "订阅即表示同意",
        "foot_terms_link": "服务条款",
        "foot_legal_mid": "与",
        "foot_refund_link": "退款政策",
        "foot_legal_suffix": "。"
    },
    "process": {
        "tag": "Process",
        "h2": "四步开通，当天即用",
        "steps": [
            {"h3": "选择方案", "p": "按使用强度选择 1x / 5x / 20x 档位与计价币种，也可先发邮件咨询。"},
            {"h3": "Stripe 订阅", "p": "在 Stripe 安全结账页选择偏好国家区域，完成月度或年度订阅付款。"},
            {"h3": "环境交付", "p": "当天为您分配高配置 Mac 物理机器与独立账户（20x 可整机独享）并完成工作空间配置，发送连接凭证与使用说明。"},
            {"h3": "持续运营", "p": "账单续费、环境维护与异常排查由我们持续托管。"}
        ]
    },
    "faq": {
        "tag": "FAQ",
        "h2": "常见问题",
        "items": [
            {
                "q": "Zaokit ClaudeOps 由谁运营？",
                "a_html": "Zaokit ClaudeOps 由澳大利亚注册公司运营，通过 Stripe 安全结算，每笔付款均自动生成正式收据与账单（Invoice），支持全球 19 种主流语言界面。"
            },
            {
                "q": "1x / 5x / 20x 与 Team / Business 方案有什么区别？按年付费有什么优惠？",
                "a_html": "全系五档方案在席位规模、物理机隔离级别、响应时段与附加权益上逐级进阶，且<strong>全系选择按年付费均仅收 10 个月费用（立省 2 个月）</strong>：<br>• <strong>1x 标准版</strong>：单人基础用量额度 + Mac mini 物理环境（独立 macOS 账户隔离）+ <strong>7×8 小时</strong>一对一专属支持；<br>• <strong>5x 专业版</strong>：单人 5 倍用量额度 + 高配置 Mac mini 物理环境（独立 macOS 账户隔离）+ <strong>7×16 小时</strong>一对一优先支持；<br>• <strong>20x 旗舰版</strong>：单人 20 倍用量额度 + 高配置 Mac Studio / Mac mini（可开启整机独享）+ <strong>7×24 小时</strong>私人顾问通道 + <strong>自建高速 RustDesk 专线</strong> + <strong>6 TB 云存储</strong>；<br>• <strong>Team 团队版（5 席 · 整机独享）</strong>：可选全员 Pro (1x)、Max (5x) 或 Ultra (20x) 规格，配备高配物理 Mac 整机团队独享、公司级席位流转管理、自建 RustDesk 团队专线、6–12 TB 云存储与 7×24h 团队顾问群；<br>• <strong>Business 企业版（10 席 · 多机集群）</strong>：可选全员 Pro (1x)、Max (5x) 或 Ultra (20x) 规格，配备多台物理 Mac 专属集群（支持 9 国双区域混合部署与快速迁移）、商业形式发票、企业级 RustDesk 独立中继、12–30 TB 云存储与 7×24h VIP 响应群；<br>• <strong>单席位弹性升配包</strong>：支持先订阅 Pro 或 Max 团队底座，再通过单席位升配包（可在结账页自选席位数量）将指定成员随时升级至 Max (5x) 或 Ultra (20x)，灵活实现任意席位混搭；<br>• <strong>ClaudeOps 企业专线增值包</strong>：面向 1x（+$5/月）与 5x（+$20/月）用户提供企业精品 BGP 跨境加速与 0% 丢包保障（20x / Team / Business 已免费内置，无需重复购买）。"
            },
            {
                "q": "什么是 ClaudeOps 企业专线增值服务？哪些用户需要加购？",
                "a_html": "<strong>ClaudeOps 企业专线</strong>是我们为跨境高频远程连接打造的企业精品 BGP 加速增值服务，结合自建低延迟中继与双段 BBR 抗丢包算法，解决跨洲/跨境公网在晚高峰时段的延迟波动与丢包掉帧问题：<br>• <strong>1x 企业专线（$5 / 月 · 年付 $50 / 年）</strong>：适配 1x 标准版单席日常远程桌面（Apple Screen Sharing）、SSH 终端与轻量开发；<br>• <strong>5x 企业专线（$20 / 月 · 年付 $200 / 年）</strong>：适配 5x 专业版重度研发，提供 5 倍高并发带宽配额与高优先级 QoS 队列，单位带宽成本立省 20%；<br>• <strong>免购说明</strong>：<strong>20x 旗舰版、Team 团队版及 Business 企业版已免费包含企业专线权益</strong>，无需额外加购。"
            },
            {
                "q": "为什么 Zaokit ClaudeOps 的定价高于普通云桌面或共享方案？",
                "a_html": "因为我们交付的是<strong>确定性的高规格物理基础设施与全托管工程服务</strong>，而非廉价的共享机房或拼单账号。每一份订阅背后都包含四项真实硬成本：<br>• <strong>高配置物理 Mac 实机</strong>：全系部署于高配置 Mac Studio / Mac mini 物理机（非虚拟化云主机），具备极强的本地算力与长期稳定运行能力，20x 起支持整机独享；<br>• <strong>上下对等 200Mbps–500Mbps+ 原生大带宽</strong>：9 国节点全部接入当地原生商业/住宅宽带，提供充裕的上下行对等带宽，远程屏幕共享依然高清跟手，告别共享小水管的卡顿与掉帧；<br>• <strong>企业精品 BGP 跨境骨干网</strong>：自建高速中继并接入香港/亚太企业级 BGP 精品骨干，配合双段 BBR 抗丢包优化，将跨国远程延迟与丢包率压至极低水平；<br>• <strong>足额官方订阅 + 7×16 / 7×24 真人运维</strong>：包含官方足额额度、账单代管、iCloud/Google Drive 云存储托管，以及工程师一对一环境调优与全天候异常排查。"
            },
            {
                "q": "账户隔离和整机独享有什么区别？为什么 1x / 5x 只能用 Apple 屏幕共享？",
                "a_html": "• <strong>独立账户隔离（1x / 5x）</strong>：多位用户共用一台高配置 Mac，每人拥有独立的 macOS 账户、文件目录与权限，数据互不可见。为保障每位用户的隐私与安全，仅开放 <strong>Apple 原生屏幕共享（Screen Sharing）</strong>访问，它会为每个账户创建相互隔离的独立桌面会话，您的屏幕与操作不会被他人看到。<br>• <strong>整机独享（20x 可开启）</strong>：整台物理 Mac 只为您一人服务，硬件、系统与网络完全专属，可自由安装任意软件、调整系统级配置，并支持<strong>任意远程桌面方式</strong>：Apple 屏幕共享、RealVNC / TigerVNC 等第三方 VNC，或我们自建的高速 RustDesk 专线（20x 免费赠送）。<br><strong>为什么多用户环境不开放第三方远程软件？</strong>RustDesk 与多数第三方 VNC 抓取的是整台 Mac 的主屏幕会话，在多用户机器上可能让他人看到甚至操作您的桌面。因此我们只在整机独享模式下开放这些工具，这是保护您隐私的安全设计。"
            },
            {
                "q": "我该选哪一档？",
                "a_html": "日常对话、写作选 1x；每天使用 Claude Code 写代码选 5x；需要多个 Agent 并行、全天候高强度使用，或需要整机独享与 RustDesk 等任意远程软件，选 20x。不确定的话可以先从低档开始，随时升级。"
            },
            {
                "q": "“确定性的稳定环境”具体指什么？",
                "a_html": "指专属独立工作空间 + 固定的高配置 Mac 物理运行环境 + 专人托管账单续费与日常运维。我们通过规范化的工程运维消除环境中断、配置冲突与续费失败等不确定因素，让您获得可预期的使用体验。"
            },
            {
                "q": "我具体该如何使用？是登录远程 Mac 物理机还是本地调用？",
                "a_html": "<strong>两种使用模式均完美支持，您可以按工作习惯自由选择：</strong><br>1. <strong>远程桌面直连</strong>：1x / 5x 通过 macOS 自带的 Apple 屏幕共享（Screen Sharing）登录您的独立账户，隔离安全、即开即用；20x 开启整机独享后，还可使用 RealVNC、TigerVNC 等第三方 VNC，或我们<strong>自建的高速 RustDesk 专线通道（20x 免费赠送）</strong>，画面更流畅、延迟更低。两种方式都提供完整的原生 macOS 图形界面与终端，长周期任务挂机无忧。<br>2. <strong>本地开发工作流无缝协同</strong>：支持在本地工作流与开发工具中无缝协同远端部署好的开发环境，免去繁琐的本地环境依赖与配置维护，让远程原生 Mac 实例成为您本机的专属算力后端。"
            },
            {
                "q": "代码和项目数据的安全与隐私如何保障？",
                "a_html": "1x / 5x 为每位用户分配独立的 macOS 账户，文件目录、权限与桌面会话相互隔离，并仅通过 Apple 原生屏幕共享访问，杜绝屏幕被他人查看；20x 可开启整机独享，整台高配置 Mac Studio 或 Mac mini 只为您一人服务，从硬件边界彻底隔离。您的会话历史、仓库源码与环境变量仅存储在您的账户或专属机器中；同时支持您自主设置访问密钥与本地加密策略，运维团队仅负责底层机器连通与账单托管，不会主动访问您账户内的数据，仅在系统维护、安全事件处置或经您授权排障时进行必要操作。"
            },
            {
                "q": "运行环境的机器与网络部署在哪里？",
                "a_html": "我们的高配置 Mac Studio 与高配置 Mac mini 物理机分布在<strong>澳大利亚、美国、新加坡、马来西亚、印尼、日本、柬埔寨、新西兰和加拿大</strong>九个国家，全部接入<strong>当地原生宽带网络环境（非廉价公共云共享机房）</strong>，具备极佳的连通纯净度与长期稳定性。在 Stripe 结账页可直接选择您偏好的国家区域，开通时为您分配固定的物理机器与独立账户（20x 可整机独享），长期稳定使用，不随意切换。"
            },
            {
                "q": "Google Drive 和 iCloud 云存储托管是如何开通的？",
                "a_html": "提供 2 TB（$8.99/月）、6 TB（$28.99/月）、12 TB（$58.99/月）和 30 TB（$148.99/月）四档容量。在 Stripe 结账页可直接选择 <strong>Apple iCloud+</strong> 或 <strong>Google Drive (Google One)</strong> 并备注您的账号邮箱，由专人 7×16 小时一对一协助完成专属云存储空间配置与账单续费托管，到期自动维护无需操心。"
            },
            {
                "q": "可以中途升级或降级吗？",
                "a_html": "可以。下一个计费周期即可调整档位，如需当月立即升级，联系我们按差价处理。"
            },
            {
                "q": "出现异常怎么办？",
                "a_html": "遇到无法使用等异常情况，第一时间联系我们，会优先排查处理，确保您的使用尽快恢复。"
            },
            {
                "q": "支持哪些付款方式？可以开具 Invoice 吗？",
                "a_html": "支持通过 Stripe 在线订阅支付（支持 Visa、Mastercard、Amex、银联 UnionPay、Apple Pay、Google Pay、Link 等主流国际与银联支付方式，支持澳元、美元、欧元、新西兰元、加元、新加坡元、人民币计价；银联卡用户可选择人民币计价，付款更顺畅），付款后 Stripe 自动生成正式收据与账单（Invoice）。如需企业多账号采购方案，请发送邮件联系咨询。"
            },
            {
                "q": "如何带机加入或作为全球伙伴加入算力网络，共享资源赚钱并点亮更多城市？",
                "a_html": "我们诚挚邀请世界各地的伙伴加入到我们的算力网络中，真正服务全球 80 亿人！<strong>您可以带机加入，共享您的资源。帮助您赚钱的同时，为别人点亮梦想的可能！</strong>无论您拥有闲置或高配的物理 Mac 设备、当地优质的原生宽带网络条件，还是连接本地开发者与创作者社区的生态资源，欢迎随时发送邮件至 <a href=\"mailto:jason2023zhang@gmail.com?subject=%E5%B8%A6%E6%9C%BA%E5%8A%A0%E5%85%A5%20Zaokit%20%E5%85%A8%E7%90%83%E7%AE%97%E5%8A%9B%E7%BD%91%E7%BB%9C%20-%20%E5%85%B1%E4%BA%AB%E8%B5%84%E6%BA%90%E7%82%B9%E4%BA%AE%E5%9F%8E%E5%B8%82\" style=\"color:var(--primary-strong);font-weight:600\">jason2023zhang@gmail.com</a> 注明您所在的国家/城市与设备或网络简况，欢迎您的加入！"
            }
        ]
    },
    "partner": {
        "eyebrow": "GLOBAL COMPUTE PARTNER · 全球算力网络共创计划",
        "h2_html": "邀请世界各地的伙伴加入我们的算力网络，<br><em class=\"grad\">真正服务全球 80 亿人！</em>",
        "p_html": "从已点亮的 9 国 13+ 核心城市出发，我们正在把纯净原生算力与最先进的 AI 生产力带向世界的每一个角落。<strong>您可以带机加入，共享您的资源。帮助您赚钱的同时，为别人点亮梦想的可能！</strong>无论您身处哪一座城市，欢迎您的加入——直接发邮件给我们，一起点亮下一座城市。",
        "chips": [
            "✦ 带机加入 · 共享 Mac 算力持续创收",
            "✦ 全球城市原生宽带资源共享",
            "✦ 集群托管与区域开发者生态合作"
        ],
        "btn": "发邮件带机/合作加入：jason2023zhang@gmail.com →"
    },
    "cta": {
        "h2": "AI 让世界无界，即刻开启最先进的生产力",
        "p": "加入全球已点亮城市的创造者网络——支持 Stripe 在线订阅当天交付，为您带来最 TOP 的 Claude 体验。",
        "btn_primary": "立即选择方案订阅",
        "btn_secondary": "发送邮件咨询：jason2023zhang@gmail.com",
        "tg_qr_aria": "打开 Telegram @letcode2020",
        "tg_qr_alt": "Telegram 二维码 @letcode2020",
        "tg_h3": "Telegram 直接聊",
        "tg_p": "扫码或点击添加，售前咨询、技术支持与 AI 资讯都在这里。"
    },
    "footer": {
        "brand": "Claude 代运营 · Zaokit ClaudeOps",
        "entity": "由澳大利亚注册公司运营 · 支持全球 19 种主流语言",
        "contact_label": "联系：",
        "alt_label": "备用：",
        "rights": "保留所有权利。",
        "products_h4": "Zaokit 产品矩阵",
        "follow_h4": "关注我们",
        "terms": "服务条款",
        "refund": "退款政策",
        "privacy": "隐私政策",
        "disclaimer": "独立第三方声明：Zaokit 为独立的云工作站托管与 AI 工程技术顾问服务商，与 Anthropic PBC、Apple Inc. 或 Google LLC 无隶属、官方授权或合作关系。页面所涉 Claude、Claude Code、Mac、iCloud、Google Drive 等名称及商标均归其各自所有者所有，仅用于描述兼容环境与托管咨询范围。"
    },
    "js": {
        "per_month": "/ 月",
        "per_year": "/ 年",
        "per_seat_mo": "/ 席 / 月",
        "per_seat_yr": "/ 席 / 年",
        "per_mo_short": "/ 月",
        "per_yr_short": "/ 年",
        "title_12mo": "按月付 12 个月总价",
        "title_reg_mo": "常规月付价",
        "note_annual": "年付仅收 10 个月 · 折合 {sym}{eq} / 月，立省 {sym}{save}",
        "note_1x_mo": "含 Claude 运行环境 · 约 {sym}{day} / 天",
        "note_20x_promo": "活动期内订阅，续费延续特惠价 · 单位成本约为 1x 的 {ratio}%",
        "note_mult_mo": "含 Claude 运行环境 · {mult} 倍额度，单位成本约为 1x 的 {ratio}%",
        "ent_team_mo": "含 5 个 {label} 独立席位 · 整机物理独享 + 统一账单与运维",
        "ent_biz_mo": "含 10 个 {label} 独立席位 · 多机物理集群独享 + VIP 专属群",
        "line_0_mo": "全天候 BGP 抗丢包直连 · 随主套餐托管",
        "line_1_mo": "5 倍优先带宽吞吐 · 高优先级 QoS 队列",
        "ent_copy": {
            "pro": {
                "label": "Pro (1x)",
                "teamBadge": "含 5 席 Pro (1x) · 团队整机独享",
                "bizBadge": "企业旗舰 · 10 席 Pro (1x) 多机集群",
                "teamSeatLi": "包含 <strong>5 个 Pro (1x) 标准成员席位</strong>（每人独立 Claude 空间与 macOS 账户）",
                "bizSeatLi": "包含 <strong>10 个 Pro (1x) 标准成员席位</strong>（支持按需弹性扩容至 50+ 席位）",
                "teamStorage": "免费赠送 6 TB 团队云存储权益（Google Drive / iCloud+）",
                "bizStorage": "免费赠送 12 TB 企业级云存储权益（Google Drive / iCloud+）"
            },
            "max": {
                "label": "Max (5x)",
                "teamBadge": "含 5 席 Max (5x) · 团队整机独享",
                "bizBadge": "企业旗舰 · 10 席 Max (5x) 多机集群",
                "teamSeatLi": "包含 <strong>5 个 Max (5x) 专业研发席位</strong>（每人独立 Claude 空间与 macOS 账户）",
                "bizSeatLi": "包含 <strong>10 个 Max (5x) 专业研发席位</strong>（支持按需弹性扩容至 50+ 席位）",
                "teamStorage": "免费赠送 12 TB 团队云存储权益（Google Drive / iCloud+）",
                "bizStorage": "免费赠送 30 TB 企业级云存储权益（Google Drive / iCloud+）"
            },
            "ultra": {
                "label": "Ultra (20x)",
                "teamBadge": "含 5 席 Ultra (20x) · 顶配整机独享",
                "bizBadge": "企业旗舰 · 10 席 Ultra (20x) 顶配集群",
                "teamSeatLi": "包含 <strong>5 个 Ultra (20x) 顶配旗舰席位</strong>（每人独立 Claude 空间与 macOS 账户）",
                "bizSeatLi": "包含 <strong>10 个 Ultra (20x) 顶配旗舰席位</strong>（支持按需弹性扩容至 50+ 席位）",
                "teamStorage": "免费赠送 12 TB 团队云存储权益（Google Drive / iCloud+）",
                "bizStorage": "免费赠送 30 TB 企业级云存储权益（Google Drive / iCloud+）"
            }
        },
        "toast_copied": "邮箱已复制：{email}，正在打开邮件客户端…",
        "toast_fallback": "请发送邮件至：{email}"
    },
    "legal_common": {
        "back_home": "← 返回首页",
        "footer_copy": "© Zaokit AI · 由澳大利亚注册公司运营"
    },
    "privacy": {
        "title": "隐私政策 | Zaokit ClaudeOps",
        "description": "Zaokit ClaudeOps 隐私政策",
        "h1": "隐私政策",
        "meta": "生效日期：2026 年 11 月 3 日 · 如各语言版本存在差异，以英文版本为准。",
        "lead_html": "本政策说明我们在提供 Zaokit ClaudeOps 服务时如何收集、使用、存储与保护您的个人信息。我们参照澳大利亚《1988 年隐私法》（Privacy Act 1988）及澳大利亚隐私原则（APPs）处理个人信息。",
        "sections": [
            {
                "h2": "1. 我们收集的信息",
                "body_html": "<ul><li><strong>联系与账户信息</strong>：姓名或称呼、邮箱地址、结账时选择的偏好区域。</li><li><strong>付款信息</strong>：由 Stripe 处理。我们不会接触或存储您的完整银行卡号，仅可查看交易记录、收据与付款状态。</li><li><strong>服务所需信息</strong>：您为开通服务提供的第三方账号邮箱（如 Claude、Google、Apple 账号），以及我们为您分配的访问凭证。</li><li><strong>沟通记录</strong>：您通过邮件、Telegram 等渠道与我们沟通的内容。</li><li><strong>网站访问数据</strong>：通过 Google Analytics、Umami 等统计工具收集的设备、浏览器、IP 地址、访问页面等信息。</li></ul>"
            },
            {
                "h2": "2. 信息的使用",
                "body_html": "<p>我们仅将上述信息用于：开通与交付服务、账单与续费处理、技术支持与沟通、保障系统安全与防范滥用、履行法律义务，以及改进网站与服务。我们不会出售您的个人信息。</p>"
            },
            {
                "h2": "3. 您运行环境中的数据",
                "body_html": "<p>您在运行环境中存储的文件、代码与会话内容属于您本人。我们不会主动访问这些内容，仅在系统维护、安全事件处置、法律要求或经您授权排障时进行必要操作。</p>"
            },
            {
                "h2": "4. 信息的共享",
                "body_html": "<p>我们仅在以下情况向第三方提供必要信息：</p><ul><li>为完成服务所必需的服务商，例如支付处理（Stripe）、网站统计、网络与基础设施服务商；</li><li>为您办理第三方订阅时，向相应服务商提供必要信息；</li><li>依据法律、法规或政府机关的合法要求。</li></ul>"
            },
            {
                "h2": "5. 跨境处理",
                "body_html": "<p>我们的运行环境分布在澳大利亚、美国、新加坡、马来西亚、印尼、日本、柬埔寨、新西兰与加拿大，Stripe 等服务商也可能在其他国家处理数据。因此，您的信息可能在您所在国家或地区之外存储或处理。我们会采取合理措施保护这些信息。</p>"
            },
            {
                "h2": "6. 信息保留",
                "body_html": "<ul><li>联系、账户与账单信息：在服务期间保留，并在服务结束后按税务、会计等法律要求的期限保留。</li><li>运行环境中的数据：服务终止后，我们可能在 7 天后删除。</li></ul>"
            },
            {
                "h2": "7. 信息安全",
                "body_html": "<p>我们采取合理的技术与管理措施保护您的信息，例如访问控制与账户隔离。但互联网传输与存储无法做到绝对安全，我们无法保证信息绝对不会被未经授权地访问。</p>"
            },
            {
                "h2": "8. Cookie 与统计",
                "body_html": "<p>本网站使用统计工具了解访问情况，这些工具可能使用 Cookie 或类似技术。您可以在浏览器设置中禁用 Cookie，这不会影响您浏览本网站。</p>"
            },
            {
                "h2": "9. 您的权利",
                "body_html": "<p>您可以联系我们查阅、更正或删除您的个人信息（法律要求保留的除外）。如您对我们的处理方式有异议，请先联系我们；如未能妥善解决，您可以向澳大利亚信息专员办公室（OAIC）投诉。</p>"
            },
            {
                "h2": "10. 政策更新",
                "body_html": "<p>我们可能不时更新本政策，更新后的版本将发布在本页面。重大变更将通过邮件或网站提前通知。</p>"
            },
            {
                "h2": "11. 联系我们",
                "body_html": "<p>隐私相关问题请发送邮件至 <a href=\"mailto:jason2023zhang@gmail.com\">jason2023zhang@gmail.com</a>（备用：<a href=\"mailto:support@zaokit.ai\">support@zaokit.ai</a>）。</p>"
            }
        ]
    },
    "terms": {
        "title": "服务条款 | Zaokit ClaudeOps",
        "description": "Zaokit ClaudeOps 服务条款",
        "h1": "服务条款",
        "meta": "生效日期：2026 年 11 月 3 日 · 如各语言版本存在差异，以英文版本为准。",
        "lead_html": "欢迎使用 Zaokit ClaudeOps（以下简称“我们”）。订阅或使用本服务，即表示您已阅读并同意本条款、<a href=\"refund.html\">《退款政策》</a>与<a href=\"privacy.html\">《隐私政策》</a>。如不同意，请勿订阅。",
        "sections": [
            {
                "h2": "1. 服务说明",
                "body_html": "<p>我们提供远程 Mac 运行环境托管、AI 工作空间配置、订阅账单代办与技术顾问服务（以下简称“本服务”）。我们是独立服务商，与 Anthropic PBC、Apple Inc.、Google LLC 不存在隶属、授权或合作关系。</p>"
            },
            {
                "h2": "2. 第三方服务",
                "body_html": "<ol><li>Claude、Google Drive、iCloud+ 等第三方服务由相应服务商提供，受其自身条款与政策约束。相关账号登记在您本人名下、归您所有，您应自行遵守该服务商的服务条款、使用政策及地区要求，并确认您的使用符合您所在地的法律。</li><li>我们仅代为办理订阅与续费，不对第三方服务的可用性、功能、用量上限、模型版本或政策变更作任何保证。套餐中的“1x / 5x / 20x”及团队/企业席位配置为参考规格，实际可用量以第三方服务商当时的规则为准。</li><li>如第三方服务商对您的账号进行限制、暂停或终止，或调整其产品、额度与价格，我们会尽合理努力协助处理，但不对由此造成的影响承担责任。</li></ol>"
            },
            {
                "h2": "3. 运行环境",
                "body_html": "<ol><li><strong>1x / 5x（多用户机器）</strong>：每位用户使用独立的 macOS 账户，仅可通过 Apple 屏幕共享访问。您不得尝试访问其他用户的账户或数据，不得安装远程控制、屏幕录制、网络代理或其他可能影响其他用户的软件。</li><li><strong>20x / Team / Business（整机或专属集群独享）</strong>：20x 可开启整机独享；Team 与 Business 方案为贵司团队独享整机或多机物理集群，并为每位成员分配独立的 macOS 账户。您可在合理范围内自行安装软件、调整系统配置，并自行承担由此造成的稳定性或安全问题。</li><li>机器型号、配置与所在区域按实际资源分配。我们会尽量满足您在结账时选择的偏好区域，但不作保证。出于维护、故障处置或资源调整的需要，我们可能迁移您的环境，并会尽量提前通知（紧急情况除外）。</li></ol>"
            },
            {
                "h2": "4. 可接受使用",
                "body_html": "<p>您不得利用本服务从事以下行为：</p><ul><li>任何违法活动，或侵犯他人知识产权、隐私及其他合法权益的行为；</li><li>发送垃圾信息、网络攻击、端口扫描、传播恶意软件；</li><li>加密货币挖矿，或与本服务目的无关的持续高负载计算；</li><li>转售、转租本服务，或与他人共享访问凭证；</li><li>违反第三方服务商条款或使用政策的行为。</li></ul><p>如您违反上述约定，我们可立即暂停或终止服务，已付费用不予退还。</p>"
            },
            {
                "h2": "5. 支持服务",
                "body_html": "<p>各套餐标注的支持时段（7×8 / 7×16 / 7×24 小时）是指我们受理与处理请求的时间范围。我们将尽合理努力及时响应，但不承诺具体的响应或解决时限。</p>"
            },
            {
                "h2": "6. 可用性与维护",
                "body_html": "<p>本服务按“现状”和“现有”基础提供。我们会尽合理努力保持稳定，但不保证服务不中断、无错误。计划内维护会尽量提前通知。因断电、网络运营商故障、第三方服务中断、自然灾害或其他超出我们合理控制范围的原因造成的中断，不视为我们违约。</p>"
            },
            {
                "h2": "7. 数据与备份",
                "body_html": "<ol><li>您对账户内的数据负责，并应自行定期备份重要数据。我们不对数据丢失承担责任，法律另有规定的除外。</li><li>我们不会主动访问您账户内的内容，仅在系统维护、安全事件处置、法律要求或经您授权排障时进行必要操作。</li><li>服务终止后，我们可能在 7 天后删除您的账户与数据，请在此之前完成导出。</li></ol>"
            },
            {
                "h2": "8. 费用与续费",
                "body_html": "<ol><li>本服务支持按月或按年订阅，通过 Stripe 自动续费，具体价格与计费周期以结账页显示为准。单席位升配包仅适用于已持有有效 Team 或 Business 底座订阅的团队账户；ClaudeOps 企业专线增值包需配合有效主套餐使用（20x、Team 及 Business 方案已默认包含）。</li><li>我们可能调整价格，并将至少提前 30 天通知。您可在新价格生效前取消订阅。</li><li>促销价格仅适用于在活动期内完成订阅的用户。订阅持续有效期间，续费按促销价格计费，但仍适用第 8.2 条。取消后重新订阅，按届时价格计费。</li><li>退款与取消规则详见<a href=\"refund.html\">《退款政策》</a>。</li></ol>"
            },
            {
                "h2": "9. 暂停与终止",
                "body_html": "<p>您可随时取消订阅，服务持续至当期结束。如您违反本条款、未按时付费，或您的使用造成安全风险，我们可暂停或终止服务。我们也可在提前 30 天通知后停止提供本服务，并按比例退还已付但未使用的费用。</p>"
            },
            {
                "h2": "10. 责任限制",
                "body_html": "<p>在法律允许的最大范围内：（a）我们不对任何间接、附带、特殊或后果性损失（包括利润、数据、商誉或业务损失）承担责任；（b）我们就本服务承担的全部责任，以您在引起索赔的事件发生前一个月内实际支付给我们的费用为上限。</p><p>本条款不排除、限制或修改您依据《澳大利亚消费者法》（Australian Consumer Law）享有的、依法不可排除的权利与保障。在法律允许限制的情况下，我们的责任限于重新提供相关服务，或支付重新提供相关服务的费用。</p>"
            },
            {
                "h2": "11. 条款变更",
                "body_html": "<p>我们可能不时更新本条款。重大变更将通过邮件或网站提前通知。变更生效后您继续使用本服务，即视为接受更新后的条款。</p>"
            },
            {
                "h2": "12. 适用法律",
                "body_html": "<p>本条款适用澳大利亚法律。</p>"
            },
            {
                "h2": "13. 联系我们",
                "body_html": "<p>如对本条款有任何疑问，请发送邮件至 <a href=\"mailto:jason2023zhang@gmail.com\">jason2023zhang@gmail.com</a>（备用：<a href=\"mailto:support@zaokit.ai\">support@zaokit.ai</a>）。</p>"
            }
        ]
    },
    "refund": {
        "title": "退款政策 | Zaokit ClaudeOps",
        "description": "Zaokit ClaudeOps 退款与取消政策",
        "h1": "退款政策",
        "meta": "生效日期：2026 年 11 月 3 日 · 如各语言版本存在差异，以英文版本为准。",
        "lead_html": "本政策说明订阅的取消与退款规则，是<a href=\"terms.html\">《服务条款》</a>的组成部分。本政策不排除您依据《澳大利亚消费者法》享有的、依法不可排除的权利。",
        "sections": [
            {
                "h2": "1. 取消订阅",
                "body_html": "<p>本服务支持按月或按年订阅，您可随时取消。取消后，服务持续至当前计费周期（当月或当年）结束，到期后不再自动续费。如需取消，请发送邮件联系我们。</p>"
            },
            {
                "h2": "2. 环境交付前",
                "body_html": "<p>如您在我们交付运行环境与访问凭证之前取消，我们将全额退款。</p>"
            },
            {
                "h2": "3. 环境交付后",
                "body_html": "<p>开通服务时，我们已为您分配专属硬件与席位资源，并代为办理相关第三方订阅。因此，环境交付后当前计费周期（含按月或按年优惠预付周期）的费用一般不予退还，也不按天或按月折算，下文第 4 条或法律另有规定的除外。</p>"
            },
            {
                "h2": "4. 因我们原因导致的服务中断",
                "body_html": "<p>如因我们的原因导致服务连续不可用超过 72 小时，我们将按不可用天数顺延您的服务期。如您希望因此取消订阅，可申请按比例退还当期未使用部分的费用。</p>"
            },
            {
                "h2": "5. 因第三方原因导致的影响",
                "body_html": "<p>因第三方服务商（包括但不限于 Anthropic、Google、Apple）的政策调整、用量限制、账号限制或服务中断造成的影响，不属于我们的原因，已代付的第三方费用不予退还。我们会尽合理努力协助您处理。</p>"
            },
            {
                "h2": "6. 云存储与企业专线增值服务",
                "body_html": "<p>云存储及 ClaudeOps 企业专线增值服务开通后，当期费用不予退还。取消后，服务持续至当期结束。</p>"
            },
            {
                "h2": "7. 违规终止",
                "body_html": "<p>因违反<a href=\"terms.html\">《服务条款》</a>而被暂停或终止服务的，已付费用不予退还。</p>"
            },
            {
                "h2": "8. 如何申请退款",
                "body_html": "<ol><li>请发送邮件至 <a href=\"mailto:jason2023zhang@gmail.com\">jason2023zhang@gmail.com</a>，注明订阅邮箱、Stripe 收据编号与申请原因。</li><li>我们会在 5 个工作日内回复。</li><li>经确认的退款将原路退回您的付款方式，到账时间以银行或支付机构为准。</li></ol>"
            },
            {
                "h2": "9. 关于拒付",
                "body_html": "<p>如对扣款有疑问，请先联系我们，我们会尽快处理。未经沟通直接向银行发起拒付（Chargeback）的，我们可能在争议处理期间暂停相关服务。</p>"
            }
        ]
    }
}


if __name__ == "__main__":
    extract_shared()
    with open(os.path.join(LOCALES_DIR, "en.json"), "w", encoding="utf-8") as f:
        json.dump(EN_LOCALE, f, ensure_ascii=False, indent=2)
    with open(os.path.join(LOCALES_DIR, "zh.json"), "w", encoding="utf-8") as f:
        json.dump(ZH_LOCALE, f, ensure_ascii=False, indent=2)
    print("Wrote locales/en.json and locales/zh.json successfully!")
