<template>
  <div class="documentation">
    <div class="doc-header">
      <h1 class="doc-title">
        <span class="gradient-text">AI Resume & CV Builder</span>
      </h1>
      <p class="doc-subtitle">
        AI-powered Resume Optimizer and CV Generator using Generative AI.
      </p>
    </div>

    <div class="doc-content">
      <!-- Features Section -->
      <section class="doc-section">
        <h2 class="section-title">
          <i class="icon">🚀</i>
          Features
        </h2>
        <div class="features-grid">
          <div class="feature-card">
            <div class="feature-icon">📄</div>
            <h3>Generate JSON</h3>
            <p>Save your form data as JSON for easy reuse and future updates</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <h3>Generate Resume</h3>
            <p>Create AI-optimized resumes tailored to specific job descriptions</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">📋</div>
            <h3>Generate CV</h3>
            <p>Generate professional CVs from your input data</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">📤</div>
            <h3>Upload File</h3>
            <p>Load previously saved JSON data to quickly populate forms</p>
          </div>
        </div>
      </section>

      <!-- Architecture Section -->
      <section class="doc-section">
        <h2 class="section-title">
          <i class="icon">🏗️</i>
          Architecture
        </h2>
        <div class="architecture-grid">
          <div class="arch-card backend">
            <h3>Backend (FastAPI)</h3>
            <ul>
              <li><strong>Framework:</strong> FastAPI with Python</li>
              <li><strong>AI Model:</strong> Qwen3 8B (quantized from deepseek-r1-0528)</li>
              <li><strong>Template Engine:</strong> Jinja2 for LaTeX rendering</li>
              <li><strong>PDF Generation:</strong> LaTeX compilation</li>
            </ul>
          </div>
          <div class="arch-card frontend">
            <h3>Frontend (Vue.js)</h3>
            <ul>
              <li><strong>Framework:</strong> Vue 3 with Vite</li>
              <li><strong>State Management:</strong> Pinia</li>
              <li><strong>API Communication:</strong> Axios</li>
              <li><strong>Development Tools:</strong> Vue DevTools</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- AI Optimization Section -->
      <section class="doc-section">
        <h2 class="section-title">
          <i class="icon">🤖</i>
          AI Optimization
        </h2>
        <div class="ai-info">
          <p>The application uses a quantized <strong>Qwen3 8B model</strong> (derived from deepseek-r1-0528) to:</p>
          <div class="ai-features">
            <div class="ai-feature">
              <span class="ai-icon">🔍</span>
              <span>Analyze job descriptions and company requirements</span>
            </div>
            <div class="ai-feature">
              <span class="ai-icon">⚡</span>
              <span>Optimize resume content for better job matching</span>
            </div>
            <div class="ai-feature">
              <span class="ai-icon">🎯</span>
              <span>Enhance keyword relevance and formatting</span>
            </div>
            <div class="ai-feature">
              <span class="ai-icon">📈</span>
              <span>Improve overall resume effectiveness</span>
            </div>
          </div>
        </div>
      </section>

      <!-- Technology Stack Section -->
      <section class="doc-section">
        <h2 class="section-title">
          <i class="icon">🛠️</i>
          Technology Stack
        </h2>
        <div class="tech-stack">
          <div class="tech-category">
            <h3>Backend</h3>
            <div class="tech-tags">
              <span class="tech-tag">FastAPI</span>
              <span class="tech-tag">Python</span>
              <span class="tech-tag">Jinja2</span>
              <span class="tech-tag">LaTeX</span>
              <span class="tech-tag">AI/ML</span>
            </div>
          </div>
          <div class="tech-category">
            <h3>Frontend</h3>
            <div class="tech-tags">
              <span class="tech-tag">Vue.js 3</span>
              <span class="tech-tag">Vite</span>
              <span class="tech-tag">Pinia</span>
              <span class="tech-tag">Axios</span>
            </div>
          </div>
        </div>
      </section>

      <!-- How It Works Section -->
      <section class="doc-section">
        <h2 class="section-title">
          <i class="icon">📝</i>
          How It Works
        </h2>
        <div class="workflow">
          <div class="workflow-step">
            <div class="step-number">1</div>
            <div class="step-content">
              <h4>Data Input</h4>
              <p>Users fill out a comprehensive form with their professional information</p>
            </div>
          </div>
          <div class="workflow-step">
            <div class="step-number">2</div>
            <div class="step-content">
              <h4>AI Processing</h4>
              <p>The system analyzes job descriptions and optimizes resume content using the Qwen3 8B model</p>
            </div>
          </div>
          <div class="workflow-step">
            <div class="step-number">3</div>
            <div class="step-content">
              <h4>Template Rendering</h4>
              <p>Data is processed through LaTeX templates using Jinja2</p>
            </div>
          </div>
          <div class="workflow-step">
            <div class="step-number">4</div>
            <div class="step-content">
              <h4>PDF Generation</h4>
              <p>High-quality PDF documents are generated using LaTeX compilation</p>
            </div>
          </div>
          <div class="workflow-step">
            <div class="step-number">5</div>
            <div class="step-content">
              <h4>Download</h4>
              <p>Users receive optimized resumes/CVs ready for job applications</p>
            </div>
          </div>
        </div>
      </section>

      <!-- Use Cases Section -->
      <section class="doc-section">
        <h2 class="section-title">
          <i class="icon">🎯</i>
          Use Cases
        </h2>
        <div class="use-cases">
          <div class="use-case">
            <h4>👔 Job Seekers</h4>
            <p>Create tailored resumes for specific job applications</p>
          </div>
          <div class="use-case">
            <h4>💼 Career Professionals</h4>
            <p>Maintain multiple resume versions for different roles</p>
          </div>
          <div class="use-case">
            <h4>🎓 Students</h4>
            <p>Generate professional CVs for academic and internship applications</p>
          </div>
          <div class="use-case">
            <h4>🔍 Recruiters</h4>
            <p>Understand optimal resume formatting and content structure</p>
          </div>
        </div>
      </section>

      <!-- Deployment Section -->
      <section class="doc-section">
        <h2 class="section-title">
          <i class="icon">📦</i>
          Deployment
        </h2>
        <div class="deployment-info">
          <p>This application is deployed on <strong>Hugging Face Spaces</strong> using Docker runtime. The frontend is served directly from the FastAPI backend, providing a seamless single-deployment solution.</p>
        </div>
      </section>
    </div>
  </div>
</template>

<style scoped>
.documentation {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  line-height: 1.6;
  color: #333;
}

.doc-header {
  text-align: center;
  margin-bottom: 3rem;
  padding: 2rem 0;
}

.doc-title {
  font-size: 3rem;
  font-weight: 800;
  margin-bottom: 1rem;
}

.gradient-text {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.doc-subtitle {
  font-size: 1.25rem;
  color: #666;
  max-width: 600px;
  margin: 0 auto;
}

.doc-section {
  margin-bottom: 3rem;
  padding: 2rem;
  background: #f8fafc;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
}

.section-title {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1.75rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  color: #1a202c;
}

.icon {
  font-size: 1.5rem;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.feature-card {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  text-align: center;
  transition: transform 0.2s ease;
}

.feature-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.feature-icon {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.feature-card h3 {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #2d3748;
}

.architecture-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.arch-card {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.arch-card.backend {
  border-left: 4px solid #48bb78;
}

.arch-card.frontend {
  border-left: 4px solid #4299e1;
}

.arch-card h3 {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: #2d3748;
}

.arch-card ul {
  list-style: none;
  padding: 0;
}

.arch-card li {
  padding: 0.5rem 0;
  border-bottom: 1px solid #e2e8f0;
}

.arch-card li:last-child {
  border-bottom: none;
}

.ai-info {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.ai-features {
  margin-top: 1.5rem;
}

.ai-feature {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.75rem 0;
  border-bottom: 1px solid #e2e8f0;
}

.ai-feature:last-child {
  border-bottom: none;
}

.ai-icon {
  font-size: 1.25rem;
}

.tech-stack {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.tech-category {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.tech-category h3 {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: #2d3748;
}

.tech-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tech-tag {
  background: #667eea;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 500;
}

.workflow {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.workflow-step {
  display: flex;
  align-items: flex-start;
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.workflow-step:last-child {
  margin-bottom: 0;
}

.step-number {
  background: #667eea;
  color: white;
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  flex-shrink: 0;
}

.step-content h4 {
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #2d3748;
}

.use-cases {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.use-case {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  text-align: center;
  transition: transform 0.2s ease;
  cursor: pointer;
}
</style>