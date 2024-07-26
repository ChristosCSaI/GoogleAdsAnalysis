# Create a new PowerPoint presentation
prs = Presentation()

# Title Slide
slide = prs.slides.add_slide(prs.slide_layouts[0])
title = slide.shapes.title
subtitle = slide.placeholders[1]
title.text = "Google Ads Performance Analysis"
subtitle.text = "Summary and Recommendations"

# Summary Slide
slide = prs.slides.add_slide(prs.slide_layouts[1])
title, content = slide.shapes.title, slide.placeholders[1]
title.text = "Overall Performance Summary"
content.text = (
    "Summarized the overall performance metrics over the two-month period, including:\n"
    "- Clicks\n"
    "- Impressions\n"
    "- CTR\n"
    "- Cost\n"
    "- Average Position\n"
    "- Conversions\n"
    "- Cost per Conversion\n"
    "- Conversion Rate\n"
    "- View-through Conversions\n"
    "- Total Conversion Value"
)

# Visualizations: Clicks, Impressions, and Cost over Time
slide = prs.slides.add_slide(prs.slide_layouts[5])
title = slide.shapes.title
title.text = "Daily Clicks, Impressions, and Cost"
slide.shapes.add_picture('/mnt/data/daily_metrics.png', Inches(0.5), Inches(1.5), width=Inches(9))

# Add descriptive text for daily metrics
description = slide.shapes.add_textbox(Inches(0.5), Inches(5.5), Inches(9), Inches(1))
description_text_frame = description.text_frame
description_text_frame.text = (
    "The daily trends show fluctuations in clicks, impressions, and cost over the two-month period. "
    "Significant spikes or drops in these metrics can indicate the impact of specific campaigns or external factors."
)
