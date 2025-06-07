# AI-RESUME_CV-Builder

A Full Stack AI-powered Resume Optimizer and CV Generator application that helps users create professional resumes tailored to specific job descriptions using advanced AI optimization.

## 🚀 Features

- **Generate JSON**: Save your form data as JSON for easy reuse and future updates
- **Generate Resume**: Create AI-optimized resumes tailored to specific job descriptions
- **Generate CV**: Generate professional CVs from your input data
- **Upload File**: Load previously saved JSON data to quickly populate forms

## 🏗️ Architecture

This application consists of two main components:

### Backend (FastAPI)
- **Framework**: FastAPI with Python
- **AI Model**: Qwen3 8B model (quantized from deepseek-r1-0528) for resume optimization
- **Template Engine**: Jinja2 for LaTeX template rendering
- **PDF Generation**: LaTeX compilation for high-quality document output

### Frontend (Vue.js)
- **Framework**: Vue 3 with Vite
- **State Management**: Pinia
- **API Communication**: Axios for backend integration
- **Development Tools**: Vue DevTools integration

## 🤖 AI Optimization

The application uses a quantized Qwen3 8B model (derived from deepseek-r1-0528) to:
- Analyze job descriptions and company requirements
- Optimize resume content for better job matching
- Enhance keyword relevance and formatting
- Improve overall resume effectiveness

## 🛠️ Technology Stack

**Backend:**
- FastAPI
- Python
- Jinja2 templating
- LaTeX for PDF generation
- AI/ML model integration

**Frontend:**
- Vue.js 3
- Vite
- Pinia (state management)
- Axios (HTTP client)

## 📦 Deployment

This application is deployed on **Hugging Face Spaces** using Docker runtime. The frontend is served directly from the FastAPI backend, providing a seamless single-deployment solution.

## 🚀 Getting Started

### Prerequisites
- Node.js (for frontend development)
- Python 3.10+ (for backend development)
- LaTeX distribution (for PDF generation)

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python main.py
```

### Frontend Development Setup

```bash
cd frontend
npm install
npm run dev
```

### Production Build

```bash
cd frontend
npm run build
```

## 📝 How It Works

1. **Data Input**: Users fill out a comprehensive form with their professional information
2. **AI Processing**: The system analyzes job descriptions and optimizes resume content using the Qwen3 8B model
3. **Template Rendering**: Data is processed through LaTeX templates using Jinja2
4. **PDF Generation**: High-quality PDF documents are generated using LaTeX compilation
5. **Download**: Users receive optimized resumes/CVs ready for job applications

## 🎯 Use Cases

- **Job Seekers**: Create tailored resumes for specific job applications
- **Career Professionals**: Maintain multiple resume versions for different roles
- **Students**: Generate professional CVs for academic and internship applications
- **Recruiters**: Understand optimal resume formatting and content structure

## 🔧 API Endpoints

The FastAPI backend provides RESTful endpoints for:
- Resume data processing
- AI-powered optimization
- PDF generation
- File upload/download functionality

## 📄 Template System

The application uses LaTeX templates with Jinja2 for:
- Professional formatting
- Consistent styling
- Customizable layouts
- High-quality PDF output

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Hugging Face Spaces for deployment platform
- Qwen3 and DeepSeek teams for the AI model
- Vue.js and FastAPI communities for excellent frameworks

---

**Live Demo**: [Available on Hugging Face Spaces](https://huggingface.co/spaces/ritik22912/AI-RESUME_CV-Builder)

**Author**: [Ritik](https://github.com/Ritik-912)