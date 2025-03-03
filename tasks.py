from crewai import Task
from agents import property_researcher

property_research_task = Task(    
    description="""Conduct a comprehensive analysis of potential retail property investments in Lahore, Pakistan.
    Specific research requirements:
    1. Market Analysis:
       - Identify top 3-5 potential retail property investment locations in Lahore
       - Analyze current market trends and economic indicators
       - Assess demographic data and consumer spending patterns
       - Evaluate Lahore's retail ecosystem and potential tenant mix

    2. Property Evaluation Criteria:
       - Foot traffic analysis in key commercial areas
       - Accessibility and transportation infrastructure (e.g., Metro Bus, Orange Line, main roads)
       - Proximity to complementary businesses and shopping hubs
       - Local economic development plans and government incentives

    3. Financial Analysis:
       - Estimate potential rental yields in Lahore's commercial zones
       - Calculate projected ROI for different retail segments
       - Assess property valuation and appreciation potential
       - Identify potential renovation or repositioning opportunities

    4. Risk Assessment:
       - Analyze competitor landscape in Lahore’s retail sector
       - Evaluate e-commerce impact on local retail businesses
       - Assess potential regulatory or zoning challenges specific to Lahore
       - Identify potential long-term growth barriers

    5. Detailed Reporting:
       Provide a comprehensive report with:
         - Executive summary
         - Detailed market insights
         - Property recommendations
         - Financial projections
         - Risk analysis
         - Visual aids (charts, graphs)

    Deliverable: A comprehensive, data-driven investment recommendation report for Lahore, Pakistan.""",
    agent=property_researcher,
    expected_output="""Detailed report containing:
    - Market analysis summary for Lahore
    - Top 3-5 recommended retail property investments
    - Comprehensive financial projections
    - Risk assessment
    - Recommendations for further due diligence""",
    # output_json=True
)
