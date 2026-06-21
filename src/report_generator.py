from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    prediction,
    servers_needed,
    risk_level,
    current_servers,
    recommendations,
    extra_cost,
    peak_day,
    peak_traffic
):

    pdf_file = "reports/traffic_report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "SmartScale AI Executive Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "<b>Prediction Summary</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Predicted Traffic: {prediction:,}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Servers Needed: {servers_needed}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Risk Level: {risk_level}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "<b>Infrastructure Status</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Current Servers: {current_servers}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Additional Servers Required: {max(0, servers_needed-current_servers)}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "<b>Cost Impact</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Estimated Monthly Cost: ₹{extra_cost:,}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "<b>Peak Forecast Day</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"{peak_day} - {peak_traffic:,} visitors",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "<b>Recommendations</b>",
            styles["Heading2"]
        )
    )

    for item in recommendations:
        content.append(
            Paragraph(
                f"• {item}",
                styles["Normal"]
            )
        )

    doc.build(content)

    return pdf_file