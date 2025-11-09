# Smart Invoice Processor

## Overview
An intelligent invoice data extraction tool that leverages Google Vision API and machine learning to automate accounts payable processing. This tool converts invoice images (JPG, PNG, PDF) into structured data, learns vendor patterns over time, and exports formatted data ready for upload to business management systems.

## 🎯 Purpose
Manual invoice data entry is time-consuming, error-prone, and costly for businesses. This tool solves that problem by:
- Automatically extracting key invoice data from images using OCR technology
- Learning and remembering vendor-specific information to improve accuracy over time
- Providing an intuitive interface for data verification and correction
- Exporting data in customizable formats for seamless system integration

## ✨ Key Features

### 🤖 AI-Powered Data Extraction
- **Google Vision API Integration**: Uses advanced OCR to extract text from invoice images. API Key replaced with placeholder text.
- **Intelligent Field Detection**: Automatically identifies vendor names, invoice numbers, dates, amounts, and more
- **Multi-Format Support**: Processes JPG, PNG, and PDF files

### 🧠 Machine Learning Capabilities
- **Vendor Pattern Recognition**: Learns and recalls vendor names and codes after first correction
- **GL Account Memory**: Remembers typical general ledger accounts and area codes for each vendor
- **Due Date Pattern Detection**: Identifies payment terms (Net 30, upon receipt, fixed dates) and auto-calculates future due dates
- **Discount Amount Learning**: Stores typical discount amounts and percentages per vendor
- **Progressive Accuracy**: Gets smarter with each processed invoice

### ✏️ Editable Review Modal
- **Side-by-Side Verification**: View original invoice image alongside extracted data
- **Real-Time Learning**: Every correction trains the system for future accuracy
- **Incomplete Invoice Warnings**: Highlights missing required fields
- **Duplicate Detection**: Prevents accidental reprocessing of invoices

### 🛡️ Duplicate Protection
- **Real-Time Detection**: Checks for duplicates in current queue by invoice number and amount
- **Historical Tracking**: Maintains database of all previously exported invoices
- **Visual Warnings**: Clearly marks duplicate invoices with alerts
- **Manageable History**: Export history can be cleared when needed

### 📊 Customizable Export Configuration
- **Flexible Column Mapping**: Map invoice fields to your system's Excel template
- **Default Values**: Set default values for columns that don't change
- **Auto-Generated Record IDs**: Sequential numbering for easy tracking
- **Reorderable Columns**: Arrange columns to match your import requirements
- **Save/Load Templates**: Store multiple export configurations

### 💾 Data Persistence
- **Learning Data Export/Import**: Transfer learned patterns between systems or share with team
- **Template Storage**: Save export configurations for reuse
- **Historical Duplicate Database**: Maintains processing history across sessions


## 🛠️ Technologies Used
- **HTML5**: Modern semantic structure
- **Tailwind CSS**: Responsive, professional styling
- **JavaScript (ES6+)**: Core application logic
- **Google Vision API**: OCR and text detection
- **LocalStorage API**: Client-side data persistence
- **Lucide Icons**: Professional icon library

## 📋 How to Use

### 1. Upload Invoices
- Click the upload area or drag-and-drop invoice images
- Supports batch uploading of multiple files
- Supported formats: JPG, PNG, PDF

### 2. Process with Google Vision
- Click "Process with Google Vision" button
- Watch real-time progress indicators
- System automatically extracts data from each invoice
-  ## ⚙️ Configuration Requirements

   ### Google Vision API Key
   This tool requires a Google Cloud Vision API key. To set up:
   1. Create a Google Cloud account at https://console.cloud.google.com
   2. Enable Vision API
   3. Generate an API key
   4. Replace 'YOUR_API_KEY_HERE' on line 11 of index.html with your key

   **For Employers**: A live demo with working API integration is available upon request.

### 3. Review & Correct Data
- Review the processed invoices list
- Click "Edit" on any invoice to verify/correct data
- The tool learns from every correction you make
- Incomplete invoices are highlighted for attention

### 4. Configure Export Template (One-Time Setup)
- Navigate to "Excel Mapping" tab
- Map extracted fields to your system's Excel columns
- Set default values for static fields
- Save template for future use

### 5. Export to CSV
- Click "Export to CSV" when ready
- File includes all processed invoices
- Formatted exactly for your business system import
- Automatically adds invoices to duplicate protection

## 🎓 Learning System Explained

### What the System Learns:
1. **Vendor Identification**: Recognizes vendor names from invoice layouts
2. **Vendor Codes**: Remembers the code assigned to each vendor
3. **GL Account Patterns**: Learns which GL accounts are typically used per vendor
4. **Area Codes**: Associates area codes with vendors
5. **Payment Terms**: Detects patterns like:
   - Net 30 (30 days from invoice date)
   - Due on specific day of month (e.g., 15th of next month)
   - Upon receipt
6. **Discount Structures**: Stores typical discount amounts and percentages

### How Learning Works:
- First time processing a vendor: Requires manual correction
- Second invoice onwards: Auto-populates learned data
- Each correction refines the pattern recognition
- Learning data can be exported and shared across team members

## 🔒 Privacy & Security
- **100% Client-Side Processing**: All data stays in your browser
- **No Server Storage**: Invoice data never uploaded to external servers (except Google Vision API for OCR)
- **Secure API Calls**: Google Vision API uses encrypted connections
- **Local Data Storage**: Learning data stored locally in browser
- **Exportable Data**: Full control over your learning database

## ⚙️ Configuration Requirements

### Google Vision API Key
This tool requires a Google Cloud Vision API key. To set up:
1. Create a Google Cloud account
2. Enable Vision API
3. Generate an API key
4. Replace the key in the code (line 11 of index.html)

**Note**: For security, consider implementing server-side API calls in production environments to protect your API key.

## 🔄 Future Enhancement Ideas
- Multi-user collaboration features
- Integration with QuickBooks, Xero, SAP
- Email-based invoice ingestion
- Advanced analytics and reporting
- Mobile app version
- Automated approval workflows
- Vendor portal integration
- Cloud-based learning data sync
---

**Note**: This tool represents a practical solution to a real business problem, showcasing both technical development skills and business process understanding.

