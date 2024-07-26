# Add ad group images to slides with descriptions
adgroup_descriptions = [
    "Ad Group 104 has a high number of clicks and conversions with a good CTR.",
    "Ad Group 536 has a very high number of clicks and impressions but a low conversion rate, indicating inefficiency.",
    "Ad Group 103 has a high CTR and conversion rate, indicating good performance.",
    "Conversions are highest for Ad Group 104, indicating effective performance.",
    "Ad Group 104 leads in CTR, showing its effectiveness in attracting clicks.",
    "Conversion rate analysis indicates that Ad Group 103 is performing well in converting clicks into actions."
]

for (title, img_path), desc in zip(adgroup_images, adgroup_descriptions):
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    slide.shapes.title.text = title
    slide.shapes.add_picture(img_path, Inches(0.5), Inches(1.5), width=Inches(9))
    description = slide.shapes.add_textbox(Inches(0.5), Inches(5.5), Inches(9), Inches(1))
    description_text_frame = description.text_frame
    description_text_frame.text = desc
