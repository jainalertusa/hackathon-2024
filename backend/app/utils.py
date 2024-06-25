from fpdf import FPDF, HTMLMixin
from typing import Optional

class PDF(FPDF, HTMLMixin):
    pass

def generate_pdf(property, features):
    pdf = PDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    # Calculate overall_score
    safety = features.safety if features.safety else 0
    school_count = features.schoolCount if features.schoolCount else 0
    sidewalk_score = features.sideWalkScore / 100 if features.sideWalkScore else 0
    transit_score = features.transitScore / 100 if features.transitScore else 0
    weather_score = features.weatherScore if features.weatherScore else 0

    overall_score = (safety + school_count / 5 + sidewalk_score + transit_score + weather_score) / 5

    # HTML content for Property Details
    html_content_property = f"""
    <h1 style="text-align:center;">Property Details</h1>
    <table class="property-table" border="1">
        <tr>
            <td><b>ID</b></td>
            <td>{property.id}</td>
        </tr>
        <tr>
            <td><b>House Type</b></td>
            <td>{property.houseType if property.houseType else ''}</td>
        </tr>
        <tr>
            <td><b>Address</b></td>
            <td>{property.address if property.address else ''}</td>
        </tr>
        <tr>
            <td><b>Price</b></td>
            <td>${property.price if property.price else ''}</td>
        </tr>
        <tr>
            <td><b>Beds</b></td>
            <td>{property.beds if property.beds else ''}</td>
        </tr>
        <tr>
            <td><b>Baths</b></td>
            <td>{property.baths if property.baths else ''}</td>
        </tr>
        <tr>
            <td><b>Sqft</b></td>
            <td>{property.sqft if property.sqft else ''}</td>
        </tr>
        <tr>
            <td><b>Parking</b></td>
            <td>{property.parking if property.parking else ''}</td>
        </tr>
        <tr>
            <td><b>Construction</b></td>
            <td>{property.construction if property.construction else ''}</td>
        </tr>
        <tr>
            <td><b>Price Per Sqft</b></td>
            <td>${property.pricePerSqft if property.pricePerSqft else ''}</td>
        </tr>
        <tr>
            <td><b>HOA Fees</b></td>
            <td>${property.homeOwnersAssociationFees if property.homeOwnersAssociationFees else ''}</td>
        </tr>
        <tr>
            <td><b>Tax</b></td>
            <td>${property.tax if property.tax else ''}</td>
        </tr>
        <tr>
            <td><b>Tax Year</b></td>
            <td>{property.taxYear if property.taxYear else ''}</td>
        </tr>
    </table>
    """

    # HTML content for Analytics Information
    html_content_analytics = f"""
    <h1 style="text-align:center;">Analytics Information</h1>
    <table class="analytics-table" border="1">
        <tr>
            <td><b>Safety</b></td>
            <td>{features.safety}</td>
        </tr>
        <tr>
            <td><b>School Count</b></td>
            <td>{features.schoolCount}</td>
        </tr>
        <tr>
            <td><b>Sidewalk Score</b></td>
            <td>{features.sideWalkScore}</td>
        </tr>
        <tr>
            <td><b>Transit Score</b></td>
            <td>{features.transitScore}</td>
        </tr>
        <tr>
            <td><b>Weather Score</b></td>
            <td>{features.weatherScore}</td>
        </tr>
        <tr>
            <td><b>Flood</b></td>
            <td>{features.flood}</td>
        </tr>
        <tr>
            <td><b>Fire</b></td>
            <td>{features.fire}</td>
        </tr>
        <tr>
            <td><b>Wind</b></td>
            <td>{features.wind}</td>
        </tr>
        <tr>
            <td><b>Air</b></td>
            <td>{features.air}</td>
        </tr>
        <tr>
            <td><b>Heat</b></td>
            <td>{features.heat}</td>
        </tr>
    </table>
    """

    # HTML content for Overall Score
    html_content_overall_score = f"""
    <h1 style="text-align:center; color:green; font-size:16pt;">Overall Score: {overall_score:.2f}</h1>
    """

    # Combine HTML contents
    html_content = html_content_property + html_content_analytics + html_content_overall_score

    # Write HTML content to PDF
    pdf.write_html(html_content)

    # Save the PDF
    pdf_file_path = f"{property.address.replace(' ', '_') if property.address else 'property'}.pdf"
    pdf.output(pdf_file_path)

    return pdf_file_path
