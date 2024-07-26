# Add campaign images to slides with descriptions
descriptions = [
    "Campaign 1 has the highest number of clicks and conversions with a relatively low cost per conversion.",
    "Campaign 15 has a very high number of impressions but a low CTR, indicating that while the ads are being displayed frequently, they are not being clicked as often.",
    "Campaign 7 has a high cost per conversion, suggesting it might be less efficient compared to other campaigns.",
    "Conversions are highest for Campaign 1, indicating effective performance.",
    "Campaign 1 also leads in CTR, showing its effectiveness in attracting clicks.",
    "Conversion rate analysis indicates that Campaign 1 is performing well in converting clicks into actions."
]

for (title, img_path), desc in zip(campaign_images, descriptions):
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    slide.shapes.title.text = title
    slide.shapes.add_picture(img_path, Inches(0.5), Inches(1.5), width=Inches(9))
    description = slide.shapes.add_textbox(Inches(0.5), Inches(5.5), Inches(9), Inches(1))
    description_text_frame = description.text_frame
    description_text_frame.text = desc
