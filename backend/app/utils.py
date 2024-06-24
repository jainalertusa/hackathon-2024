from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Property Report', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def property_table(self, property):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Property Details', 0, 1, 'L')
        self.ln(10)
        self.set_font('Arial', '', 12)
        
        row_height = self.font_size + 2  # Row height

        data = [
            ('ID', property.id),
            ('House Type', property.houseType if property.houseType else ''),
            ('Address', property.address if property.address else ''),
            ('Price', f"${property.price if property.price else ''}"),
            ('Beds', property.beds if property.beds else ''),
            ('Baths', property.baths if property.baths else ''),
            ('Sqft', property.sqft if property.sqft else ''),
            ('Parking', property.parking if property.parking else ''),
            ('Construction', property.construction if property.construction else ''),
            ('Price Per Sqft', f"${property.pricePerSqft if property.pricePerSqft else ''}"),
            ('HOA Fees', f"${property.homeOwnersAssociationFees if property.homeOwnersAssociationFees else ''}"),
            ('Tax', f"${property.tax if property.tax else ''}"),
            ('Tax Year', property.taxYear if property.taxYear else '')
        ]

        # Determine the width of each column
        col_widths = [self.get_string_width(str(item)) + 4 for row in data for item in row]
        col_width = max(col_widths)

        for row in data:
            self.set_font('Arial', 'B', 12)
            self.cell(col_width, row_height, str(row[0]), border=1)
            self.set_font('Arial', '', 12)
            self.cell(col_width, row_height, str(row[1]), border=1)
            self.ln(row_height)

        self.ln(10)  # Extra space after Property Details table

    def analytics_table(self, features, overall_score):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Analytics Information', 0, 1, 'L')
        self.ln(10)
        self.set_font('Arial', '', 12)
        
        row_height = self.font_size + 2  # Row height

        data = [
            ('Safety', features.safety),
            ('School Count', features.schoolCount),
            ('Sidewalk Score', features.sideWalkScore),
            ('Transit Score', features.transitScore),
            ('Weather Score', features.weatherScore),
            ('Flood', features.flood),
            ('Fire', features.fire),
            ('Wind', features.wind),
            ('Air', features.air),
            ('Heat', features.heat)
        ]

        # Determine the width of each column
        col_widths = [self.get_string_width(str(item)) + 4 for row in data for item in row]
        col_width = max(col_widths)

        for row in data:
            self.set_font('Arial', 'B', 12)
            self.cell(col_width, row_height, str(row[0]), border=1)
            self.set_font('Arial', '', 12)
            self.cell(col_width, row_height, str(row[1]), border=1)
            self.ln(row_height)

        self.ln(10)  # Ensure no extra blank space after table

    def overall_score(self, score):
        self.set_text_color(0, 128, 0)  # Green color
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, f'Overall Score: {score:.2f}', 0, 1, 'L')
        self.set_text_color(0, 0, 0)  # Reset to default color
        self.ln(10)

def generate_pdf(property, features):
    pdf = PDF()
    pdf.add_page()

    # Calculate overall_score
    safety = features.safety
    school_count = features.schoolCount / 5
    sidewalk_score = features.sideWalkScore / 100
    transit_score = features.transitScore / 100
    weather_score = features.weatherScore / 10

    overall_score = (safety + school_count + sidewalk_score + transit_score + weather_score) / 5

    # Add property details table
    pdf.property_table(property)

    # Add analytics information table
    pdf.analytics_table(features, overall_score)

    # Add overall score
    pdf.overall_score(overall_score)

    # Save the PDF
    pdf_file_path = f"{property.address.replace(' ', '_') if property.address else 'property'}.pdf"
    pdf.output(pdf_file_path)

    return pdf_file_path
