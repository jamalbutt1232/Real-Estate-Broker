from crewai import Task
from agents import property_researcher,property_analyst

property_research_task = Task(    
    description="""Conduct a comprehensive analysis of potential retail property investments in Pakistan.
    Specific research requirements:
    1. Market Analysis:
       - Identify top 3-5 potential retail property investment locations in Pakistan
       - Analyze current market trends and economic indicators
       - Assess demographic data and consumer spending patterns
       - Evaluate Pakistan's retail ecosystem and potential tenant mix

    2. Property Evaluation Criteria:
       - Foot traffic analysis in key commercial areas
       - Accessibility and transportation infrastructure (e.g., Metro Bus, Orange Line, main roads)
       - Proximity to complementary businesses and shopping hubs
       - Local economic development plans and government incentives

    3. Financial Analysis:
       - Estimate potential rental yields in Pakistan's commercial zones
       - Calculate projected ROI for different retail segments
       - Assess property valuation and appreciation potential
       - Identify potential renovation or repositioning opportunities

    4. Risk Assessment:
       - Analyze competitor landscape in Pakistan’s retail sector
       - Evaluate e-commerce impact on local retail businesses
       - Assess potential regulatory or zoning challenges specific to Pakistan
       - Identify potential long-term growth barriers

    5. Detailed Reporting:
       Provide a comprehensive report with:
         - Executive summary
         - Detailed market insights
         - Property recommendations
         - Financial projections
         - Risk analysis
         - Visual aids (charts, graphs)

    Deliverable: A comprehensive, data-driven investment recommendation report for Pakistan.""",
    agent=property_researcher,
    expected_output="""Detailed report containing:
    - Market analysis summary for Pakistan
    - Top 3-5 recommended retail property investments
    - Comprehensive financial projections
    - Risk assessment
    - Recommendations for further due diligence""",
    output_file="research_task_output.txt"
    # output_json=True
)


property_analysis_task = Task(
description="Summarise the property information into bullet point list. ",
    expected_output="""A detailed report of each of the cities.
    The results should ALWAYS be formatted as shown below: 

    City 1: Name of the city
    Mean Price: $1,200,000
    Rental Vacancy: x%
    Rental Yield: y%
    Background Information: These cities are typically located near major transport hubs, 
    employment centers, and educational institutions. 
    The following list highlights some of the top contenders for investment opportunities """,
agent=property_analyst,
output_file="property_analysis_report.txt"
)