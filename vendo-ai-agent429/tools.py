from crewai_tools import tool

class VendoAITools:
    @tool("Recommend Products")
    def recommend_products(self, customer_profile: str) -> str:
        """Generates personalized product recommendations."""
        return f"""Product Recommendations for {customer_profile}:

Top Recommendations:
1. Premium Wireless Headphones ($299)
   - Match score: 95%
   - Based on: Previous audio purchases, price range
   - Reviews: 4.7/5 (2,340 reviews)

2. Smart Fitness Watch ($249)
   - Match score: 88%
   - Based on: Fitness interest, tech affinity
   - Reviews: 4.6/5 (1,892 reviews)

3. Portable Bluetooth Speaker ($129)
   - Match score: 82%
   - Based on: Audio preferences, portability need
   - Reviews: 4.5/5 (3,456 reviews)

Also Consider:
- Wireless Earbuds ($179, 78% match)
- Noise Cancelling Headphones ($349, 76% match)

Confidence: High (based on 15 data points)"""

    @tool("Answer Product Questions")
    def answer_product_questions(self, question: str) -> str:
        """Answers customer questions about products."""
        return f"""Answer to: {question}

The Premium Wireless Headphones feature:

Battery Life: 30 hours with ANC off, 20 hours with ANC on
Connectivity: Bluetooth 5.2, multipoint connection
Audio: 40mm drivers, Hi-Res Audio certified
ANC: Hybrid active noise cancellation
Comfort: Memory foam ear cups, adjustable headband
Weight: 250g
Warranty: 2 years

Perfect for:
- Long commutes (excellent battery)
- Travel (great ANC)
- Music enthusiasts (Hi-Res Audio)

Not ideal for:
- Intense workouts (over-ear design)
- Very tight budgets (premium price)

Customer satisfaction: 94% would recommend"""

    @tool("Compare Products")
    def compare_products(self, products: str) -> str:
        """Compares multiple products side-by-side."""
        return f"""Product Comparison: {products}

Feature | Headphones | Earbuds | Speaker
--------|------------|---------|--------
Price   | $299      | $179    | $129
Battery | 30 hours  | 8 hours | 12 hours
ANC     | Yes       | Yes     | No
Portability | Medium | High   | High
Sound Quality | Excellent | Very Good | Good
Waterproof | No | IPX4 | IPX7
Use Case | Home/Travel | Active | Outdoor

Best for Commute: Headphones (battery + ANC)
Best for Gym: Earbuds (portable + secure fit)
Best for Outdoors: Speaker (waterproof + loud)

Recommendation: Based on your daily commute, the
Headphones offer best value with superior ANC and
battery life."""

    @tool("Analyze Customer Behavior")
    def analyze_customer_behavior(self, data: str) -> str:
        """Analyzes customer behavior patterns."""
        return f"""Customer Behavior Analysis:

Purchase Patterns:
- Frequency: 2-3 purchases/month
- Average order value: $245
- Preferred categories: Electronics (60%), Home (25%)
- Shopping time: Evenings (7-10pm), Weekends

Browsing Behavior:
- Session duration: 18 minutes avg
- Pages per visit: 8.5
- Research pattern: Reads 4-5 reviews before purchase
- Price sensitivity: Moderate (willing to pay for quality)

Engagement:
- Email open rate: 42% (above avg)
- Click-through rate: 8.5%
- Social media follower: Yes (Instagram)
- Loyalty program: Gold tier

Insights:
- High-value customer (top 15%)
- Quality-focused buyer
- Responsive to email campaigns
- Likely to purchase premium products"""

    @tool("Predict Preferences")
    def predict_preferences(self, customer_id: str) -> str:
        """Predicts customer preferences using ML."""
        return f"""Preference Predictions - Customer {customer_id}:

Product Categories (Probability):
- Audio devices: 85% (strong interest)
- Smart home: 72% (growing interest)
- Fitness tech: 68% (moderate interest)
- Gaming: 45% (occasional)
- Fashion: 32% (low interest)

Price Sensitivity:
- Willing to pay premium: 78%
- Sweet spot: $200-$400
- Rarely purchases <$50 items

Brand Preferences:
- Sony: 92% affinity
- Apple: 85% affinity
- Samsung: 78% affinity
- Generic brands: 25% affinity

Purchase Timing:
- Next purchase window: 7-14 days
- Confidence: 73%
- Likely trigger: New product launch

Recommendation: Focus on premium audio and
smart home products from Sony/Apple."""

    @tool("Segment Customers")
    def segment_customers(self, customer_base: str) -> str:
        """Segments customers into meaningful groups."""
        return f"""Customer Segmentation:

Segment 1: Tech Enthusiasts (25%)
- High AOV: $350
- Frequent purchases
- Early adopters
- Premium products
- Strategy: Exclusive previews, premium line

Segment 2: Value Seekers (35%)
- Moderate AOV: $120
- Deal-driven
- Comparison shoppers
- Mid-range products
- Strategy: Promotions, bundles

Segment 3: Occasional Buyers (30%)
- Low AOV: $80
- Infrequent purchases
- Need-based shopping
- Budget products
- Strategy: Engagement campaigns

Segment 4: High Rollers (10%)
- Very high AOV: $850
- Luxury buyers
- Brand loyal
- Premium/luxury products
- Strategy: VIP service, personalization

Target Priority: Segments 1 & 4 (highest LTV)"""

    @tool("Optimize Pricing")
    def optimize_pricing(self, product: str) -> str:
        """Optimizes product pricing for maximum revenue."""
        return f"""Pricing Optimization - {product}:

Current Price: $299
Market Analysis:
- Competitor range: $249-$349
- Market median: $289
- Premium positioning: Valid

Price Elasticity: -1.8 (elastic)
- 10% price decrease → +18% sales
- 10% price increase → -18% sales

Optimal Pricing:
- Revenue maximization: $319 (+6.5% revenue)
- Volume maximization: $269 (+23% volume)
- Balanced approach: $289 (+4.2% revenue, +8% volume)

Recommendations:
- Regular price: $299 (current)
- Sale price: $269 (holidays, +volume)
- Premium bundle: $399 (with accessories)
- Early bird: $279 (new launches)

Dynamic Pricing:
- Peak season: $319
- Off-season: $269
- Clearance: $229

Expected Impact: +8% revenue with balanced approach"""

    @tool("Create Promotions")
    def create_promotions(self, goals: str) -> str:
        """Creates promotional campaigns."""
        return f"""Promotion Strategy - {goals}:

Campaign 1: "Summer Sound Sale"
- Discount: 20% off audio products
- Duration: 7 days
- Target: All customers
- Expected lift: +35% sales
- Budget: $5,000 (advertising)

Campaign 2: "Bundle & Save"
- Offer: Headphones + Speaker 15% off
- Duration: 30 days
- Target: High-value customers
- Expected AOV: +25%
- Budget: $2,000

Campaign 3: "Loyalty Rewards"
- Offer: Double points weekend
- Duration: 3 days
- Target: Loyalty members
- Expected engagement: +40%
- Budget: $1,000

Campaign 4: "Email Exclusive"
- Offer: Early access + 10% off
- Duration: 48 hours
- Target: Email subscribers
- Expected conversion: +15%
- Budget: $500

Total Budget: $8,500
Expected Revenue: $45,000
ROI: 430%"""

    @tool("Suggest Upsells")
    def suggest_upsells(self, cart_items: str) -> str:
        """Suggests upsell and cross-sell opportunities."""
        return f"""Upsell/Cross-sell Suggestions:

Current Cart: {cart_items}

Upsell Opportunities:
1. Upgrade to Premium Model (+$50)
   - Better features, 4.8/5 rating
   - 35% of customers upgrade
   - Conversion rate: 35%

2. Extended Warranty (+$39)
   - 3-year protection
   - Accident coverage
   - Conversion rate: 22%

Cross-sell Suggestions:
3. Protective Case ($29)
   - Perfect fit guarantee
   - 65% attach rate
   - Conversion rate: 65%

4. Charging Accessories ($35)
   - Fast charger + cable
   - 40% attach rate
   - Conversion rate: 40%

5. Cleaning Kit ($19)
   - Maintenance essentials
   - 28% attach rate
   - Conversion rate: 28%

Recommended Bundle:
Product + Case + Warranty = $367 (was $397)
Save $30, +$68 AOV increase
Bundle conversion: 45%"""

    @tool("Generate Sales Report")
    def generate_sales_report(self, period: str) -> str:
        """Generates comprehensive sales performance report."""
        return f"""SALES PERFORMANCE REPORT - {period}

EXECUTIVE SUMMARY:
Strong sales performance with 12% growth. Conversion rate
improved to 3.8%. AI recommendations drove 35% of revenue.

KEY METRICS:
- Total Revenue: $145,000 (+12% YoY)
- Orders: 525 (+8% YoY)
- Average Order Value: $276 (+4%)
- Conversion Rate: 3.8% (+0.5pp)
- Customer Acquisition Cost: $42 (-15%)

AI PERFORMANCE:
- Recommendation click-through: 28%
- AI-assisted purchases: 35% of revenue
- Upsell success rate: 32%
- Cross-sell attachment: 45%

TOP PRODUCTS:
1. Premium Headphones: $52,000 (36%)
2. Smart Watch: $28,000 (19%)
3. Wireless Earbuds: $21,000 (14%)

CUSTOMER SEGMENTS:
- Tech Enthusiasts: $58,000 (40%)
- Value Seekers: $35,000 (24%)
- High Rollers: $32,000 (22%)

CONVERSION FUNNEL:
- Visitors: 13,800
- Product views: 8,280 (60%)
- Add to cart: 1,656 (12%)
- Purchases: 525 (3.8%)

OPPORTUNITIES:
- Cart abandonment: 68% (improve checkout)
- Email campaigns: 15% CTR (scale up)
- Mobile optimization: 45% of traffic (enhance)"""

    @tool("Calculate Conversion Metrics")
    def calculate_conversion_metrics(self, data: str) -> str:
        """Calculates detailed conversion and performance metrics."""
        return f"""Conversion Metrics Analysis:

OVERALL CONVERSION:
- Visitor to purchase: 3.8%
- Add-to-cart rate: 12%
- Cart-to-purchase: 32%
- Benchmark: Industry avg 2.5-3%
- Performance: Above average

CHANNEL PERFORMANCE:
- Organic search: 4.2% conversion
- Paid search: 3.5% conversion
- Email: 6.8% conversion (best)
- Social: 2.1% conversion
- Direct: 5.2% conversion

DEVICE BREAKDOWN:
- Desktop: 4.5% conversion
- Mobile: 3.2% conversion
- Tablet: 3.9% conversion
- Opportunity: Mobile optimization

AI FEATURES:
- Recommendation clicks: 28% CTR
- Recommendation purchases: 15% conversion
- AI chat usage: 12% of sessions
- Chat-assisted conversion: 8.5%

CUSTOMER TYPE:
- New customers: 2.8% conversion
- Returning: 6.2% conversion
- Loyalty members: 9.5% conversion

OPTIMIZATION OPPORTUNITIES:
- Reduce cart abandonment: +125 sales
- Improve mobile UX: +85 sales
- Scale email campaigns: +65 sales
- Potential revenue increase: +$75,000"""

    @tool("Recommend Strategies")
    def recommend_strategies(self, analysis: str) -> str:
        """Recommends strategic improvements."""
        return f"""Strategic Recommendations:

IMMEDIATE ACTIONS (0-30 days):
1. Cart abandonment emails ($0 cost)
   - Send reminder after 1 hour
   - Offer 5% discount after 24 hours
   - Expected: +8% recovery rate

2. Mobile checkout optimization ($3,000)
   - One-click checkout
   - Apple Pay/Google Pay
   - Expected: +0.8pp conversion

3. Email campaign scale-up ($2,000/mo)
   - 3x frequency (within limits)
   - Segment-specific campaigns
   - Expected: +$15,000/mo revenue

SHORT-TERM (1-3 months):
4. AI personalization enhancement ($8,000)
   - Real-time recommendations
   - Behavioral triggers
   - Expected: +1.2pp conversion

5. Loyalty program expansion ($5,000)
   - Tier benefits enhancement
   - Referral rewards
   - Expected: +25% member purchases

6. Product bundling ($0 cost)
   - Create 10 curated bundles
   - 10% bundle discount
   - Expected: +$8,000/mo

LONG-TERM (3-6 months):
7. Visual search implementation ($15,000)
   - Image-based search
   - AR try-on
   - Expected: +15% engagement

8. Predictive inventory ($10,000)
   - Demand forecasting
   - Stock optimization
   - Expected: -20% stockouts

TOTAL INVESTMENT: $43,000
EXPECTED ANNUAL RETURN: $180,000
ROI: 320%"""
