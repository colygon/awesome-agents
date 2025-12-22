from crewai import Task
from textwrap import dedent

class PersonalizedShoppingTasks:
    def analyze_customer_preferences(self, agent, customer_data, shopping_goal):
        return Task(
            description=dedent(f"""\
                Analyze customer preferences and build a comprehensive profile:

                Customer Data: {customer_data}
                Shopping Goal: {shopping_goal}

                Analyze:
                1. Style Preferences
                   - Preferred styles, colors, and patterns
                   - Brands they like
                   - Quality expectations

                2. Shopping Behavior
                   - Budget range
                   - Price sensitivity
                   - Purchase frequency
                   - Preferred retailers

                3. Product Preferences
                   - Category interests
                   - Size and fit preferences
                   - Material preferences
                   - Feature priorities

                4. Lifestyle Factors
                   - Use cases and occasions
                   - Activity level
                   - Climate considerations
                   - Storage constraints

                Create a detailed customer profile that captures preferences and constraints."""),
            agent=agent,
            expected_output="Comprehensive customer preference profile with style, budget, and lifestyle factors"
        )

    def research_products(self, agent, preferences, category, budget):
        return Task(
            description=dedent(f"""\
                Research and identify products matching customer preferences:

                Preferences: {preferences}
                Product Category: {category}
                Budget: {budget}

                Find products that:
                1. Match Style Preferences
                   - Color, pattern, style alignment
                   - Brand preferences
                   - Quality level

                2. Meet Practical Requirements
                   - Size and fit
                   - Features and functionality
                   - Material and construction

                3. Fit Budget
                   - Within price range
                   - Good value for money
                   - Worth the investment

                4. Have Good Reviews
                   - Positive customer feedback
                   - Quality ratings
                   - Reliability

                Find at least 10-15 product options from multiple retailers."""),
            agent=agent,
            expected_output="List of 10-15 products with details, pricing, and ratings from multiple retailers"
        )

    def find_best_deals(self, agent, products):
        return Task(
            description=dedent(f"""\
                Find the best deals and prices for selected products:

                Products: {products}

                For each product:
                1. Price Comparison
                   - Compare prices across retailers
                   - Identify lowest price
                   - Check shipping costs

                2. Find Discounts
                   - Available coupons
                   - Ongoing promotions
                   - Seasonal sales
                   - Loyalty discounts

                3. Track Price History
                   - Current price trend
                   - Price drop likelihood
                   - Best time to buy

                4. Calculate Total Cost
                   - Product price
                   - Shipping
                   - Taxes
                   - Discount applied

                Identify the best deals and optimal purchase timing."""),
            agent=agent,
            expected_output="Deal analysis with best prices, available discounts, and purchase timing recommendations"
        )

    def create_style_recommendations(self, agent, products, preferences):
        return Task(
            description=dedent(f"""\
                Create personalized style recommendations and combinations:

                Products: {products}
                Customer Preferences: {preferences}

                Develop:
                1. Top Product Picks
                   - Best matches for customer style
                   - Why each product fits
                   - Styling tips

                2. Product Combinations
                   - Complete outfit suggestions
                   - Mix and match options
                   - Accessory pairings

                3. Versatility Analysis
                   - How to style each piece
                   - Occasions suitable for
                   - Wardrobe integration

                4. Alternative Options
                   - Similar products at different price points
                   - Different colors/styles
                   - Complementary items

                Create a styled recommendation guide."""),
            agent=agent,
            expected_output="Styled recommendations with product combinations, versatility tips, and alternatives"
        )

    def compile_shopping_list(self, agent, recommendations, deals, budget):
        return Task(
            description=dedent(f"""\
                Compile a personalized shopping list with final recommendations:

                Product Recommendations: {recommendations}
                Deal Information: {deals}
                Budget: {budget}

                Create a comprehensive shopping guide including:

                1. Top Recommendations (Prioritized)
                   - Product name and description
                   - Why it's recommended
                   - Price and where to buy
                   - Available discounts
                   - Direct purchase link

                2. Product Details
                   - Key features
                   - Size/fit information
                   - Care instructions
                   - Customer reviews summary

                3. Styling Suggestions
                   - How to wear/use
                   - What to pair with
                   - Occasion suitability

                4. Budget Breakdown
                   - Total cost
                   - Potential savings
                   - Alternative budget options

                5. Purchase Strategy
                   - Buy now vs. wait for sale
                   - Priority order
                   - Where to get best deal

                6. Alternative Options
                   - Similar products at different price points
                   - Backup choices

                Format as an actionable, easy-to-follow shopping guide."""),
            agent=agent,
            expected_output="Complete personalized shopping guide with prioritized recommendations, pricing, styling tips, and purchase strategy"
        )
