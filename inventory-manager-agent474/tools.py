from crewai_tools import tool
import json
from typing import Dict, List, Any
from datetime import datetime, timedelta
import random

class InventoryTrackingTools:
    @tool("Check Stock Levels")
    def check_stock_levels(sku: str) -> str:
        """
        Checks current stock levels for a product SKU.
        Useful for monitoring inventory status.
        """
        # Simulated stock data
        stock_level = random.randint(0, 500)
        reorder_point = 100
        max_stock = 400

        stock_data = {
            "sku": sku,
            "product_name": f"Product {sku}",
            "current_stock": stock_level,
            "reorder_point": reorder_point,
            "max_stock": max_stock,
            "status": "critical" if stock_level < 50 else "low" if stock_level < reorder_point else "normal" if stock_level < max_stock else "overstock",
            "unit_cost": 25.00,
            "total_value": stock_level * 25.00,
            "location": ["Warehouse A - Aisle 3", "Warehouse B - Aisle 7"],
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        return json.dumps(stock_data, indent=2)

    @tool("Track Product Movement")
    def track_product_movement(sku: str) -> str:
        """
        Tracks product movements (in/out) over time.
        Useful for understanding inventory flow.
        """
        movements = []
        start_date = datetime.now() - timedelta(days=30)

        for i in range(15):
            movement_date = start_date + timedelta(days=i*2)
            movement_type = random.choice(["in", "out"])
            quantity = random.randint(10, 100)

            movements.append({
                "date": movement_date.strftime("%Y-%m-%d"),
                "type": movement_type,
                "quantity": quantity,
                "reference": f"PO-{random.randint(1000, 9999)}" if movement_type == "in" else f"SO-{random.randint(1000, 9999)}",
                "location": random.choice(["Warehouse A", "Warehouse B"])
            })

        movement_data = {
            "sku": sku,
            "period": "Last 30 days",
            "total_in": sum(m["quantity"] for m in movements if m["type"] == "in"),
            "total_out": sum(m["quantity"] for m in movements if m["type"] == "out"),
            "net_change": sum(m["quantity"] if m["type"] == "in" else -m["quantity"] for m in movements),
            "movements": movements[-5:]  # Last 5 movements
        }

        return json.dumps(movement_data, indent=2)

    @tool("Calculate Turnover Rate")
    def calculate_turnover_rate(sku: str) -> str:
        """
        Calculates inventory turnover rate for a product.
        Useful for understanding how quickly inventory sells.
        """
        # Simulated calculations
        avg_inventory = random.randint(100, 300)
        cogs_annual = random.randint(50000, 150000)
        turnover_rate = cogs_annual / (avg_inventory * 25.00)  # Assuming $25 unit cost

        turnover_data = {
            "sku": sku,
            "turnover_rate": round(turnover_rate, 2),
            "average_inventory": avg_inventory,
            "cogs_annual": cogs_annual,
            "days_of_inventory": round(365 / turnover_rate, 1),
            "classification": "fast-moving" if turnover_rate > 8 else "medium-moving" if turnover_rate > 4 else "slow-moving",
            "benchmark": {
                "industry_average": 6.5,
                "performance": "above" if turnover_rate > 6.5 else "below"
            }
        }

        return json.dumps(turnover_data, indent=2)

    @tool("Audit Inventory")
    def audit_inventory(location: str) -> str:
        """
        Performs inventory audit for a location.
        Useful for maintaining inventory accuracy.
        """
        discrepancies = random.randint(0, 5)

        audit_data = {
            "location": location,
            "audit_date": datetime.now().strftime("%Y-%m-%d"),
            "total_skus_counted": 245,
            "discrepancies_found": discrepancies,
            "accuracy_rate": round((245 - discrepancies) / 245 * 100, 2),
            "discrepancy_details": [
                {
                    "sku": f"SKU-{random.randint(1000, 9999)}",
                    "expected": 50,
                    "actual": 47,
                    "variance": -3,
                    "variance_percent": -6.0
                }
                for _ in range(min(discrepancies, 3))
            ],
            "total_value_variance": -125.50,
            "next_audit_due": (datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")
        }

        return json.dumps(audit_data, indent=2)


class ForecastingTools:
    @tool("Analyze Demand Patterns")
    def analyze_demand_patterns(sku: str) -> str:
        """
        Analyzes historical demand patterns for forecasting.
        Useful for understanding demand trends.
        """
        # Simulated demand pattern analysis
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        monthly_demand = [random.randint(80, 150) for _ in range(12)]

        pattern_analysis = {
            "sku": sku,
            "analysis_period": "12 months",
            "monthly_demand": dict(zip(months, monthly_demand)),
            "average_monthly_demand": round(sum(monthly_demand) / len(monthly_demand), 2),
            "peak_month": months[monthly_demand.index(max(monthly_demand))],
            "low_month": months[monthly_demand.index(min(monthly_demand))],
            "demand_variance": round(max(monthly_demand) - min(monthly_demand), 2),
            "trend": "increasing" if monthly_demand[-3:] > monthly_demand[:3] else "decreasing" if monthly_demand[-3:] < monthly_demand[:3] else "stable",
            "seasonality_detected": True,
            "coefficient_of_variation": 0.25
        }

        return json.dumps(pattern_analysis, indent=2)

    @tool("Predict Future Demand")
    def predict_future_demand(sku: str) -> str:
        """
        Predicts future demand for inventory planning.
        Useful for proactive inventory management.
        """
        # Simulated demand prediction
        base_demand = random.randint(80, 120)

        predictions = {
            "sku": sku,
            "forecast_date": datetime.now().strftime("%Y-%m-%d"),
            "predictions": {
                "next_30_days": {
                    "predicted_demand": base_demand,
                    "lower_bound": int(base_demand * 0.85),
                    "upper_bound": int(base_demand * 1.15),
                    "confidence": 0.85
                },
                "next_60_days": {
                    "predicted_demand": int(base_demand * 2.1),
                    "lower_bound": int(base_demand * 2.1 * 0.80),
                    "upper_bound": int(base_demand * 2.1 * 1.20),
                    "confidence": 0.75
                },
                "next_90_days": {
                    "predicted_demand": int(base_demand * 3.2),
                    "lower_bound": int(base_demand * 3.2 * 0.75),
                    "upper_bound": int(base_demand * 3.2 * 1.25),
                    "confidence": 0.65
                }
            },
            "factors_considered": [
                "Historical sales data",
                "Seasonal trends",
                "Market conditions",
                "Promotional calendar"
            ],
            "risk_level": "medium"
        }

        return json.dumps(predictions, indent=2)

    @tool("Identify Seasonal Trends")
    def identify_seasonal_trends(category: str) -> str:
        """
        Identifies seasonal patterns in product demand.
        Useful for seasonal inventory planning.
        """
        seasonal_data = {
            "category": category,
            "seasonal_patterns": {
                "Q1": {
                    "trend": "low",
                    "demand_index": 0.85,
                    "notes": "Post-holiday slowdown"
                },
                "Q2": {
                    "trend": "moderate",
                    "demand_index": 1.0,
                    "notes": "Spring season pickup"
                },
                "Q3": {
                    "trend": "high",
                    "demand_index": 1.25,
                    "notes": "Summer peak demand"
                },
                "Q4": {
                    "trend": "very_high",
                    "demand_index": 1.5,
                    "notes": "Holiday season surge"
                }
            },
            "peak_months": ["November", "December"],
            "low_months": ["January", "February"],
            "preparation_recommendations": [
                "Build inventory in Q3 for Q4 demand",
                "Clear excess stock in Q1",
                "Monitor weather patterns for seasonal items"
            ]
        }

        return json.dumps(seasonal_data, indent=2)


class OptimizationTools:
    @tool("Calculate Reorder Point")
    def calculate_reorder_point(sku: str) -> str:
        """
        Calculates optimal reorder point for a product.
        Useful for preventing stockouts.
        """
        # Simulated reorder point calculation
        avg_daily_demand = random.randint(5, 20)
        lead_time_days = random.randint(7, 21)
        safety_stock = random.randint(50, 150)

        reorder_calculation = {
            "sku": sku,
            "average_daily_demand": avg_daily_demand,
            "lead_time_days": lead_time_days,
            "safety_stock": safety_stock,
            "reorder_point": (avg_daily_demand * lead_time_days) + safety_stock,
            "formula": "ROP = (Avg Daily Demand × Lead Time) + Safety Stock",
            "service_level": "95%",
            "stockout_risk": "5%",
            "recommendations": [
                f"Reorder when stock reaches {(avg_daily_demand * lead_time_days) + safety_stock} units",
                "Monitor lead times for supplier reliability",
                "Review quarterly for demand changes"
            ]
        }

        return json.dumps(reorder_calculation, indent=2)

    @tool("Optimize Order Quantity")
    def optimize_order_quantity(sku: str) -> str:
        """
        Calculates economic order quantity (EOQ).
        Useful for minimizing total inventory costs.
        """
        # Simulated EOQ calculation
        annual_demand = random.randint(1000, 5000)
        order_cost = random.randint(50, 150)
        holding_cost_per_unit = random.uniform(2, 8)

        eoq = int((2 * annual_demand * order_cost / holding_cost_per_unit) ** 0.5)

        eoq_analysis = {
            "sku": sku,
            "economic_order_quantity": eoq,
            "annual_demand": annual_demand,
            "order_cost": order_cost,
            "holding_cost_per_unit": round(holding_cost_per_unit, 2),
            "optimal_order_frequency": round(annual_demand / eoq, 1),
            "total_annual_cost": round((annual_demand / eoq * order_cost) + (eoq / 2 * holding_cost_per_unit), 2),
            "cost_savings": {
                "vs_current_policy": 1250.00,
                "percentage": 12.5
            },
            "recommendations": [
                f"Order {eoq} units per order",
                f"Place approximately {round(annual_demand / eoq)} orders per year",
                "Consider volume discounts if available"
            ]
        }

        return json.dumps(eoq_analysis, indent=2)

    @tool("Set Safety Stock")
    def set_safety_stock(sku: str) -> str:
        """
        Determines appropriate safety stock levels.
        Useful for buffer against demand variability.
        """
        # Simulated safety stock calculation
        avg_demand = random.randint(10, 30)
        demand_std_dev = random.randint(3, 10)
        lead_time = random.randint(7, 14)
        service_level = 0.95

        z_score = 1.65  # For 95% service level
        safety_stock = int(z_score * demand_std_dev * (lead_time ** 0.5))

        safety_stock_data = {
            "sku": sku,
            "recommended_safety_stock": safety_stock,
            "average_demand": avg_demand,
            "demand_variability": demand_std_dev,
            "lead_time_days": lead_time,
            "service_level": "95%",
            "holding_cost_impact": round(safety_stock * 5.00, 2),
            "stockout_protection": f"Protects against {service_level*100}% of demand variations",
            "alternatives": {
                "90%_service_level": int(1.28 * demand_std_dev * (lead_time ** 0.5)),
                "99%_service_level": int(2.33 * demand_std_dev * (lead_time ** 0.5))
            }
        }

        return json.dumps(safety_stock_data, indent=2)

    @tool("Perform ABC Analysis")
    def perform_abc_analysis(inventory_data: str) -> str:
        """
        Performs ABC analysis to categorize inventory by value.
        Useful for prioritizing inventory management efforts.
        """
        # Simulated ABC analysis
        abc_analysis = {
            "analysis_date": datetime.now().strftime("%Y-%m-%d"),
            "total_skus": 500,
            "categories": {
                "A_items": {
                    "count": 50,
                    "percentage_of_skus": 10,
                    "percentage_of_value": 70,
                    "characteristics": "High value, tight control needed",
                    "recommended_actions": [
                        "Daily monitoring",
                        "Accurate demand forecasting",
                        "Frequent cycle counts",
                        "Strong supplier relationships"
                    ]
                },
                "B_items": {
                    "count": 150,
                    "percentage_of_skus": 30,
                    "percentage_of_value": 25,
                    "characteristics": "Moderate value, moderate control",
                    "recommended_actions": [
                        "Weekly monitoring",
                        "Regular review cycles",
                        "Periodic audits",
                        "Standard reorder procedures"
                    ]
                },
                "C_items": {
                    "count": 300,
                    "percentage_of_skus": 60,
                    "percentage_of_value": 5,
                    "characteristics": "Low value, loose control acceptable",
                    "recommended_actions": [
                        "Monthly monitoring",
                        "Simple reorder systems",
                        "Annual audits",
                        "Consider bulk ordering"
                    ]
                }
            },
            "recommendations": [
                "Focus resources on A items",
                "Automate C item reordering",
                "Review B items quarterly"
            ]
        }

        return json.dumps(abc_analysis, indent=2)

    @tool("Optimize Storage Layout")
    def optimize_storage_layout(warehouse_id: str) -> str:
        """
        Optimizes warehouse storage layout for efficiency.
        Useful for reducing picking time and costs.
        """
        layout_optimization = {
            "warehouse_id": warehouse_id,
            "current_metrics": {
                "average_pick_time": "8.5 minutes",
                "storage_utilization": "72%",
                "travel_distance_per_order": "450 feet"
            },
            "optimized_layout": {
                "fast_movers_zone": "Near shipping dock (30% of items, 70% of picks)",
                "medium_movers_zone": "Middle section (40% of items, 25% of picks)",
                "slow_movers_zone": "Back section (30% of items, 5% of picks)"
            },
            "projected_improvements": {
                "average_pick_time": "6.2 minutes (27% improvement)",
                "storage_utilization": "85% (18% improvement)",
                "travel_distance_per_order": "310 feet (31% reduction)"
            },
            "implementation_plan": [
                "Phase 1: Relocate A items to fast-mover zone",
                "Phase 2: Consolidate C items in back section",
                "Phase 3: Optimize picking routes",
                "Phase 4: Update WMS with new locations"
            ],
            "estimated_roi": {
                "implementation_cost": 15000,
                "annual_savings": 45000,
                "payback_period": "4 months"
            }
        }

        return json.dumps(layout_optimization, indent=2)
