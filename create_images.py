import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.colors import LinearSegmentedColormap

# Create directory for images if it doesn't exist
os.makedirs('/home/ubuntu/truist_website/images', exist_ok=True)

# Define Truist brand colors
truist_purple = '#241631'
truist_pink = '#F94CAF'
truist_light_purple = '#3A2A4F'
truist_dark_purple = '#1A0F24'
truist_light_pink = '#FA7AC5'
truist_dark_pink = '#D62E8B'
truist_white = '#FFFFFF'
truist_light_gray = '#F5F5F5'

# Create custom colormaps
truist_cmap = LinearSegmentedColormap.from_list('truist', [truist_purple, truist_pink])
truist_cmap2 = LinearSegmentedColormap.from_list('truist2', [truist_dark_purple, truist_purple, truist_light_purple])

# Set global plot style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']
plt.rcParams['axes.facecolor'] = truist_white
plt.rcParams['figure.facecolor'] = truist_white
plt.rcParams['axes.edgecolor'] = truist_light_gray
plt.rcParams['axes.labelcolor'] = truist_purple
plt.rcParams['xtick.color'] = truist_purple
plt.rcParams['ytick.color'] = truist_purple
plt.rcParams['grid.color'] = truist_light_gray
plt.rcParams['figure.figsize'] = (10, 6)

# 1. Create Truist logo placeholder
def create_truist_logo():
    fig, ax = plt.subplots(figsize=(4, 1.5))
    ax.text(0.5, 0.5, 'Truist', fontsize=24, fontweight='bold', 
            color=truist_purple, ha='center', va='center')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('/home/ubuntu/truist_website/images/truist-logo.png', dpi=300, bbox_inches='tight', transparent=True)
    plt.close()

# 2. Create investment vs returns chart
def create_investment_returns_chart():
    years = ['2025', '2026', '2027', '2028']
    investment = [42.4, 22.4, 13.7, 0]
    returns = [0, 35, 107, 165]
    cumulative_investment = np.cumsum(investment)
    
    fig, ax = plt.subplots()
    
    width = 0.35
    x = np.arange(len(years))
    
    ax.bar(x - width/2, investment, width, label='Annual Investment', color=truist_purple)
    ax.bar(x + width/2, returns, width, label='Annual Returns', color=truist_pink)
    
    ax.plot(x, cumulative_investment, 'o-', color=truist_dark_purple, linewidth=2, 
            label='Cumulative Investment')
    
    ax.set_xlabel('Year')
    ax.set_ylabel('Amount ($ millions)')
    ax.set_title('Investment vs. Returns (3-Year Projection)', fontweight='bold', color=truist_purple)
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/truist_website/images/investment-returns-chart.png', dpi=300, bbox_inches='tight')
    plt.close()

# 3. Create investment timeline chart
def create_investment_timeline_chart():
    categories = ['Technology\nInfrastructure', 'Software\nDevelopment', 
                 'Personnel\nand Training', 'Risk\nManagement']
    year1 = [19.4, 12.5, 7.9, 2.6]
    year2 = [8.1, 7.5, 5.3, 1.5]
    year3 = [4.9, 5.1, 2.7, 1.0]
    
    fig, ax = plt.subplots()
    
    width = 0.25
    x = np.arange(len(categories))
    
    ax.bar(x - width, year1, width, label='Year 1 (2025)', color=truist_purple)
    ax.bar(x, year2, width, label='Year 2 (2026)', color=truist_light_purple)
    ax.bar(x + width, year3, width, label='Year 3 (2027)', color=truist_pink)
    
    ax.set_xlabel('Investment Category')
    ax.set_ylabel('Amount ($ millions)')
    ax.set_title('Investment Distribution by Year', fontweight='bold', color=truist_purple)
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/truist_website/images/investment-timeline-chart.png', dpi=300, bbox_inches='tight')
    plt.close()

# 4. Create ROI projection chart
def create_roi_projection_chart():
    quarters = ['Q1\n2025', 'Q2\n2025', 'Q3\n2025', 'Q4\n2025', 
                'Q1\n2026', 'Q2\n2026', 'Q3\n2026', 'Q4\n2026',
                'Q1\n2027', 'Q2\n2027', 'Q3\n2027', 'Q4\n2027']
    
    investment = [15, 10, 10, 7.4, 6, 6, 5.4, 5, 4, 3.7, 3, 3]
    cumulative_investment = np.cumsum(investment)
    
    returns = [0, 0, 0, 5, 8, 10, 12, 15, 20, 25, 30, 32]
    cumulative_returns = np.cumsum(returns)
    
    roi_percentage = np.zeros_like(cumulative_investment)
    for i in range(len(cumulative_investment)):
        if cumulative_investment[i] > 0:
            roi_percentage[i] = (cumulative_returns[i] / cumulative_investment[i]) * 100
    
    fig, ax1 = plt.subplots()
    
    color = truist_purple
    ax1.set_xlabel('Quarter')
    ax1.set_ylabel('Amount ($ millions)', color=color)
    ax1.plot(quarters, cumulative_investment, 'o-', color=truist_purple, linewidth=2, label='Cumulative Investment')
    ax1.plot(quarters, cumulative_returns, 's-', color=truist_pink, linewidth=2, label='Cumulative Returns')
    ax1.tick_params(axis='y', labelcolor=color)
    
    # Add breakeven point
    breakeven_idx = np.where(cumulative_returns >= cumulative_investment)[0][0]
    ax1.axvline(x=breakeven_idx, color='gray', linestyle='--', alpha=0.7)
    ax1.text(breakeven_idx + 0.1, cumulative_investment[breakeven_idx] * 0.5, 
             f'Breakeven: {quarters[breakeven_idx]}', 
             rotation=90, verticalalignment='center')
    
    ax2 = ax1.twinx()
    color = truist_dark_pink
    ax2.set_ylabel('ROI (%)', color=color)
    ax2.plot(quarters, roi_percentage, '^-', color=color, linewidth=2, label='ROI %')
    ax2.tick_params(axis='y', labelcolor=color)
    
    # Combine legends
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    ax1.set_title('Cumulative ROI Projection', fontweight='bold', color=truist_purple)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/truist_website/images/roi-projection-chart.png', dpi=300, bbox_inches='tight')
    plt.close()

# 5. Create implementation timeline
def create_implementation_timeline():
    phases = ['Foundation', 'Development', 'Pilot & Testing', 'Full Deployment']
    start_months = [1, 4, 10, 16]
    durations = [3, 6, 6, 9]
    
    fig, ax = plt.subplots(figsize=(10, 4))
    
    y_positions = range(len(phases))
    colors = [truist_purple, truist_light_purple, truist_pink, truist_light_pink]
    
    for i, (phase, start, duration, color) in enumerate(zip(phases, start_months, durations, colors)):
        ax.barh(i, duration, left=start, height=0.5, color=color, alpha=0.8)
        ax.text(start + duration/2, i, phase, ha='center', va='center', color='white', fontweight='bold')
        
        # Add start and end month labels
        ax.text(start, i-0.3, f'Month {start}', ha='left', va='bottom', fontsize=8)
        ax.text(start + duration, i-0.3, f'Month {start + duration}', ha='right', va='bottom', fontsize=8)
    
    ax.set_yticks([])
    ax.set_xticks(range(0, 25, 3))
    ax.set_xlim(0, 24)
    ax.set_xlabel('Month')
    ax.set_title('Implementation Timeline Overview', fontweight='bold', color=truist_purple)
    
    # Add phase descriptions
    descriptions = ['Setup', 'Build', 'Test', 'Deploy']
    for i, desc in enumerate(descriptions):
        ax.text(start_months[i] + durations[i]/2, -0.5, desc, ha='center', fontsize=9, color=truist_purple)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/truist_website/images/implementation-timeline.png', dpi=300, bbox_inches='tight')
    plt.close()

# 6. Create development milestones chart
def create_development_milestones():
    milestones = ['NLP Model\nDevelopment', 'Personalization\nAlgorithms', 
                 'Banking System\nIntegration', 'UI/UX\nDevelopment', 
                 'Security\nImplementation', 'Testing\nFramework']
    
    start_weeks = [0, 2, 4, 8, 10, 14]
    durations = [8, 10, 12, 10, 8, 10]
    completion = [100, 100, 85, 90, 95, 80]  # percentage complete
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), gridspec_kw={'height_ratios': [3, 1]})
    
    # Gantt chart
    y_positions = range(len(milestones))
    
    for i, (milestone, start, duration) in enumerate(zip(milestones, start_weeks, durations)):
        ax1.barh(i, duration, left=start, height=0.5, color=truist_purple, alpha=0.7)
        ax1.text(start + duration/2, i, milestone, ha='center', va='center', color='white', fontweight='bold')
    
    ax1.set_yticks([])
    ax1.set_xticks(range(0, 25, 4))
    ax1.set_xlim(0, 24)
    ax1.set_xlabel('Week')
    ax1.set_title('Development Phase Milestones', fontweight='bold', color=truist_purple)
    
    # Completion percentage
    ax2.bar(milestones, completion, color=truist_pink)
    ax2.set_ylim(0, 100)
    ax2.set_ylabel('Completion %')
    ax2.set_xticklabels(milestones, rotation=45, ha='right')
    
    for i, v in enumerate(completion):
        ax2.text(i, v + 3, f"{v}%", ha='center', color=truist_purple, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/truist_website/images/development-milestones.png', dpi=300, bbox_inches='tight')
    plt.close()

# 7. Create pilot results chart
def create_pilot_results():
    categories = ['User\nSatisfaction', 'Task\nCompletion', 'Response\nAccuracy', 
                 'Response\nTime', 'Issue\nResolution']
    
    internal_pilot = [85, 92, 88, 95, 82]
    customer_pilot = [78, 85, 82, 90, 75]
    targets = [80, 90, 85, 90, 80]
    
    x = np.arange(len(categories))
    width = 0.25
    
    fig, ax = plt.subplots()
    
    ax.bar(x - width, internal_pilot, width, label='Internal Pilot', color=truist_purple)
    ax.bar(x, customer_pilot, width, label='Customer Pilot', color=truist_pink)
    ax.bar(x + width, targets, width, label='Target', color='lightgray', alpha=0.5)
    
    # Add horizontal line at 80% (minimum acceptable level)
    ax.axhline(y=80, color='gray', linestyle='--', alpha=0.7)
    ax.text(len(categories)-1, 81, 'Minimum Acceptable Level', ha='right', va='bottom', 
            color='gray', fontsize=8, style='italic')
    
    ax.set_ylabel('Score (%)')
    ax.set_title('Pilot Results Overview', fontweight='bold', color=truist_purple)
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/truist_website/images/pilot-results.png', dpi=300, bbox_inches='tight')
    plt.close()

# 8. Create adoption curve
def create_adoption_curve():
    months = range(1, 25)
    
    # S-curve adoption model
    def s_curve(x, L=100, k=0.3, x0=12):
        return L / (1 + np.exp(-k * (x - x0)))
    
    adoption_percentage = [s_curve(x) for x in months]
    
    # Different user segments
    early_adopters = [min(s_curve(x, L=100, k=0.4, x0=8), 100) for x in months]
    mainstream = [min(s_curve(x, L=100, k=0.3, x0=12), 100) for x in months]
    late_adopters = [min(s_curve(x, L=100, k=0.25, x0=16), 100) for x in months]
    
    fig, ax = plt.subplots()
    
    ax.plot(months, early_adopters, 'o-', color=truist_purple, linewidth=2, label='Digital-First Customers')
    ax.plot(months, mainstream, 's-', color=truist_pink, linewidth=2, label='Mainstream Customers')
    ax.plot(months, late_adopters, '^-', color=truist_light_purple, linewidth=2, label='Traditional Customers')
    ax.plot(months, adoption_percentage, '--', color='gray', linewidth=2, label='Overall Adoption')
    
    # Add annotations for key milestones
    ax.annotate('Pilot Launch', xy=(3, 10), xytext=(3, 20),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8))
    
    ax.annotate('Full Launch', xy=(10, 40), xytext=(10, 55),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8))
    
    ax.annotate('75% Adoption', xy=(18, 75), xytext=(18, 60),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8))
    
    ax.set_xlabel('Month')
    ax.set_ylabel('Adoption (%)')
    ax.set_title('Expected Adoption Curve', fontweight='bold', color=truist_purple)
    ax.set_xlim(1, 24)
    ax.set_ylim(0, 100)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/truist_website/images/adoption-curve.png', dpi=300, bbox_inches='tight')
    plt.close()

# 9. Create risk framework diagram
def create_risk_framework():
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create a circular diagram with concentric circles
    circle_radii = [1, 2, 3, 4]
    circle_labels = ['Governance', 'Risk\nAssessment', 'Control\nImplementation', 'Monitoring']
    circle_colors = [truist_purple, truist_light_purple, truist_pink, truist_light_pink]
    
    for radius, label, color in zip(circle_radii, circle_labels, circle_colors):
        circle = plt.Circle((0, 0), radius, fill=True, alpha=0.7, color=color)
        ax.add_patch(circle)
        ax.text(0, 0 - radius + 0.5, label, ha='center', va='center', 
                color='white', fontweight='bold', fontsize=12)
    
    # Add risk categories around the outer circle
    n_categories = 10
    theta = np.linspace(0, 2*np.pi, n_categories, endpoint=False)
    
    categories = ['Data Privacy', 'Compliance', 'Model Risk', 'Operational', 
                 'Reputational', 'Strategic', 'Ethical', 'Cybersecurity', 
                 'Customer', 'Emerging']
    
    radius = 5
    for angle, category in zip(theta, categories):
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        ax.text(x, y, category, ha='center', va='center', 
                color=truist_purple, fontweight='bold',
                bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'))
        
        # Add connecting lines
        ax.plot([0, x*0.8], [0, y*0.8], color=truist_purple, linestyle='-', linewidth=1, alpha=0.5)
    
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-5.5, 5.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    ax.set_title('Risk Management Framework', fontweight='bold', color=truist_purple, fontsize=14, pad=20)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/truist_website/images/risk-framework.png', dpi=300, bbox_inches='tight')
    plt.close()

# 10. Create three lines of defense model
def create_three_lines_defense():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create three boxes for the lines of defense
    box_positions = [1, 2, 3]
    box_labels = ['First Line\nBusiness Units', 'Second Line\nRisk Management', 'Third Line\nInternal Audit']
    box_colors = [truist_light_pink, truist_pink, truist_purple]
    
    box_width = 0.6
    box_height = 3
    
    for pos, label, color in zip(box_positions, box_labels, box_colors):
        rect = plt.Rectangle((pos - box_width/2, 1), box_width, box_height, 
                            facecolor=color, alpha=0.8, edgecolor='none')
        ax.add_patch(rect)
        ax.text(pos, 2.5, label, ha='center', va='center', 
                color='white', fontweight='bold', fontsize=12)
    
    # Add responsibilities under each box
    responsibilities = [
        ['Implement Controls', 'Execute Processes', 'Identify Risks'],
        ['Set Policy', 'Monitor Compliance', 'Report to Board'],
        ['Independent Review', 'Evaluate Effectiveness', 'Recommend Improvements']
    ]
    
    for i, (pos, resp_list) in enumerate(zip(box_positions, responsibilities)):
        for j, resp in enumerate(resp_list):
            y_pos = 0.7 - j * 0.3
            ax.text(pos, y_pos, resp, ha='center', va='center', 
                   color=truist_purple, fontsize=10,
                   bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.3'))
    
    # Add arrows connecting the boxes
    arrow_props = dict(arrowstyle='->', linewidth=2, color=truist_purple)
    
    ax.annotate('', xy=(1.35, 2.5), xytext=(1.65, 2.5), arrowprops=arrow_props)
    ax.annotate('', xy=(2.35, 2.5), xytext=(2.65, 2.5), arrowprops=arrow_props)
    
    # Add board oversight at the top
    rect = plt.Rectangle((1.5, 4.5), 1, 0.5, facecolor=truist_dark_purple, alpha=0.8, edgecolor='none')
    ax.add_patch(rect)
    ax.text(2, 4.75, 'Board Oversight', ha='center', va='center', color='white', fontweight='bold')
    
    # Add arrows from board to all three lines
    for pos in box_positions:
        ax.annotate('', xy=(pos, 4), xytext=(2, 4.5), arrowprops=arrow_props)
    
    ax.set_xlim(0.5, 3.5)
    ax.set_ylim(0, 5.5)
    ax.set_aspect('auto')
    ax.axis('off')
    
    ax.set_title('Three Lines of Defense Model', fontweight='bold', color=truist_purple, fontsize=14, pad=20)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/truist_website/images/three-lines-defense.png', dpi=300, bbox_inches='tight')
    plt.close()

# 11. Create maturity roadmap
def create_maturity_roadmap():
    stages = ['Initial', 'Developing', 'Defined', 'Managed', 'Optimized']
    domains = ['Governance', 'Risk Assessment', 'Controls', 'Monitoring', 'Incident Response']
    
    # Current and target maturity levels (1-5 scale)
    current_levels = [2, 3, 2, 2, 3]
    target_levels = [4, 5, 4, 4, 5]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x = np.arange(len(domains))
    width = 0.35
    
    ax.bar(x - width/2, current_levels, width, label='Current State', color=truist_purple)
    ax.bar(x + width/2, target_levels, width, label='Target State (Year 2)', color=truist_pink)
    
    # Add maturity stage labels
    for i in range(1, 6):
        ax.axhline(y=i, color='gray', linestyle='--', alpha=0.3)
        ax.text(len(domains) - 0.5, i, stages[i-1], ha='right', va='bottom', 
                color='gray', fontsize=8, style='italic')
    
    ax.set_ylabel('Maturity Level')
    ax.set_title('Risk Management Maturity Roadmap', fontweight='bold', color=truist_purple)
    ax.set_xticks(x)
    ax.set_xticklabels(domains)
    ax.set_yticks(range(1, 6))
    ax.set_ylim(0, 5.5)
    ax.legend()
    
    # Add arrows showing progression
    for i, (curr, targ) in enumerate(zip(current_levels, target_levels)):
        ax.annotate('', xy=(i - 0.1, targ), xytext=(i - 0.1, curr),
                   arrowprops=dict(facecolor=truist_light_pink, width=1.5, headwidth=8))
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/truist_website/images/maturity-roadmap.png', dpi=300, bbox_inches='tight')
    plt.close()

# Generate all images
create_truist_logo()
create_investment_returns_chart()
create_investment_timeline_chart()
create_roi_projection_chart()
create_implementation_timeline()
create_development_milestones()
create_pilot_results()
create_adoption_curve()
create_risk_framework()
create_three_lines_defense()
create_maturity_roadmap()

print("All images created successfully in /home/ubuntu/truist_website/images/")
