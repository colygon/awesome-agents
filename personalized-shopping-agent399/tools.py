from crewai_tools import tool
import os
import json
from typing import List, Dict
import requests

class PreferenceTools:
    @tool("Analyze preferences")
    def analyze_preferences(customer_input: str) -> str:
        """
        Analyze customer input to extract shopping preferences.
        Returns structured preference data.
        """
        preferences = {
            'style': {
                'primary_style': 'casual',
                'secondary_styles': ['modern', 'minimalist'],
                'colors': ['neutral', 'blue', 'black'],
                'patterns': ['solid', 'minimal_patterns']
            },
            'budget': {
                'range': 'medium',
                'price_sensitivity': 'moderate',
                'willing_to_splurge_on': ['quality_basics', 'versatile_pieces']
            },
            'priorities': [
                'quality',
                'versatility',
                'comfort',
                'durability'
            ],
            'brands': {
                'preferred': [],
                'avoided': []
            }
        }

        return json.dumps(preferences, indent=2)

    @tool("Build customer profile")
    def build_profile(preferences: str, history: str = "") -> str:
        """
        Build comprehensive customer profile from preferences and history.
        Returns detailed customer profile.
        """
        profile = {
            'customer_id': 'profile_001',
            'style_profile': {
                'aesthetic': 'modern_casual',
                'formality': 'casual_to_business_casual',
                'trend_adoption': 'moderate'
            },
            'size_preferences': {
                'fit': 'regular',
                'preferred_sizes': {}
            },
            'lifestyle': {
                'activity_level': 'active',
                'climate': 'temperate',
                'occasions': ['work', 'casual', 'social']
            },
            'shopping_behavior': {
                'research_level': 'high',
                'brand_loyalty': 'moderate',
                'impulse_buying': 'low'
            }
        }

        return json.dumps(profile, indent=2)

class ShoppingTools:
    @tool("Search products")
    def search_products(query: str, category: str = "all", budget: str = "") -> str:
        """
        Search for products matching criteria.
        Returns list of matching products.
        """
        # In production, integrate with e-commerce APIs
        # (Amazon Product API, Shopify, etc.)

        products = {
            'query': query,
            'category': category,
            'results': [
                {
                    'name': 'Example Product',
                    'price': 49.99,
                    'retailer': 'Example Store',
                    'rating': 4.5,
                    'reviews_count': 1250,
                    'url': 'https://example.com/product',
                    'image': 'https://example.com/image.jpg',
                    'in_stock': True,
                    'colors_available': ['Black', 'Navy', 'Gray'],
                    'sizes_available': ['S', 'M', 'L', 'XL']
                }
            ],
            'total_results': 1,
            'note': 'Integrate with e-commerce APIs for real product data'
        }

        return json.dumps(products, indent=2)

    @tool("Compare products")
    def compare_products(product_ids: str) -> str:
        """
        Compare multiple products side-by-side.
        Returns comparison data.
        """
        comparison = {
            'products': [],
            'comparison_factors': {
                'price': 'Price comparison',
                'quality': 'Quality ratings',
                'features': 'Feature comparison',
                'reviews': 'Customer review summary'
            },
            'best_value': 'Product with best quality/price ratio',
            'best_quality': 'Highest quality product',
            'best_price': 'Lowest price product'
        }

        return json.dumps(comparison, indent=2)

    @tool("Check availability")
    def check_availability(product_id: str) -> str:
        """
        Check product availability across retailers.
        Returns availability information.
        """
        availability = {
            'product_id': product_id,
            'in_stock': True,
            'retailers': [
                {
                    'name': 'Retailer A',
                    'in_stock': True,
                    'price': 49.99,
                    'shipping': 'Free over $50',
                    'delivery_time': '2-3 days'
                }
            ],
            'overall_availability': 'readily_available'
        }

        return json.dumps(availability, indent=2)

    @tool("Analyze purchase history")
    def analyze_purchase_history(customer_id: str) -> str:
        """
        Analyze customer's past purchases to understand preferences.
        Returns purchase pattern analysis.
        """
        history_analysis = {
            'customer_id': customer_id,
            'purchase_patterns': {
                'favorite_categories': ['clothing', 'accessories'],
                'favorite_brands': [],
                'average_price_point': 'medium',
                'purchase_frequency': 'monthly',
                'seasonal_patterns': 'buys more in fall/spring'
            },
            'insights': [
                'Prefers quality over quantity',
                'Values versatile pieces',
                'Interested in sustainable options'
            ]
        }

        return json.dumps(history_analysis, indent=2)

    @tool("Find deals")
    def find_deals(product_name: str) -> str:
        """
        Find deals, discounts, and promotions for products.
        Returns available deals.
        """
        deals = {
            'product': product_name,
            'available_deals': [
                {
                    'type': 'coupon',
                    'discount': '20% off',
                    'code': 'SAVE20',
                    'expiry': '2024-12-31',
                    'retailer': 'Example Store'
                },
                {
                    'type': 'sale',
                    'discount': '30% off',
                    'expiry': '2024-12-25',
                    'retailer': 'Another Store'
                }
            ],
            'best_deal': '30% off at Another Store',
            'note': 'Integrate with coupon APIs and retailer APIs for real deals'
        }

        return json.dumps(deals, indent=2)

    @tool("Track prices")
    def track_prices(product_id: str) -> str:
        """
        Track price history and predict price trends.
        Returns price tracking data.
        """
        price_tracking = {
            'product_id': product_id,
            'current_price': 49.99,
            'historical_prices': {
                '30_day_avg': 54.99,
                '90_day_avg': 52.99,
                'lowest': 44.99,
                'highest': 59.99
            },
            'price_trend': 'decreasing',
            'recommendation': 'good_time_to_buy',
            'predicted_next_sale': '2024-12-26',
            'note': 'Use price tracking APIs like CamelCamelCamel or Honey'
        }

        return json.dumps(price_tracking, indent=2)

    @tool("Apply coupons")
    def apply_coupons(cart_items: str) -> str:
        """
        Find and apply best coupons for cart items.
        Returns coupon recommendations.
        """
        coupon_recommendations = {
            'applicable_coupons': [
                {
                    'code': 'SAVE20',
                    'discount': '20% off',
                    'savings': 10.00,
                    'conditions': 'Minimum purchase $50'
                }
            ],
            'best_combination': 'SAVE20',
            'total_savings': 10.00,
            'final_total': 39.99
        }

        return json.dumps(coupon_recommendations, indent=2)

class RecommendationTools:
    @tool("Recommend products")
    def recommend_products(preferences: str, category: str) -> str:
        """
        Generate personalized product recommendations.
        Returns recommended products with reasoning.
        """
        recommendations = {
            'category': category,
            'recommended_products': [
                {
                    'product_name': 'Recommended Item',
                    'why_recommended': 'Matches your style preferences and budget',
                    'match_score': 95,
                    'price': 49.99,
                    'key_features': ['Quality material', 'Versatile', 'Durable']
                }
            ],
            'total_recommendations': 1
        }

        return json.dumps(recommendations, indent=2)

    @tool("Suggest combinations")
    def suggest_combinations(items: str) -> str:
        """
        Suggest how to combine products together.
        Returns styling combinations.
        """
        combinations = {
            'outfits': [
                {
                    'name': 'Casual Day Look',
                    'items': ['Item A', 'Item B', 'Item C'],
                    'occasion': 'Casual outings',
                    'season': 'All seasons',
                    'styling_tips': 'Pair with sneakers for comfort'
                }
            ],
            'versatility_score': 85
        }

        return json.dumps(combinations, indent=2)

    @tool("Create outfit")
    def create_outfit(occasion: str, preferences: str) -> str:
        """
        Create complete outfit for specific occasion.
        Returns curated outfit with all pieces.
        """
        outfit = {
            'occasion': occasion,
            'outfit_name': 'Perfect Casual Friday',
            'pieces': [
                {
                    'category': 'top',
                    'product': 'Classic Oxford Shirt',
                    'price': 45.00
                },
                {
                    'category': 'bottom',
                    'product': 'Dark Wash Jeans',
                    'price': 68.00
                }
            ],
            'total_cost': 113.00,
            'styling_notes': 'Roll up sleeves for casual look',
            'accessories': ['Watch', 'Belt']
        }

        return json.dumps(outfit, indent=2)

    @tool("Create shopping list")
    def create_shopping_list(recommendations: str) -> str:
        """
        Create organized shopping list from recommendations.
        Returns formatted shopping list.
        """
        shopping_list = {
            'priority_items': [],
            'optional_items': [],
            'total_budget_needed': 0,
            'stores_to_visit': [],
            'estimated_savings': 0,
            'purchase_timeline': 'Buy priority items now, wait for sales on optional items'
        }

        return json.dumps(shopping_list, indent=2)
