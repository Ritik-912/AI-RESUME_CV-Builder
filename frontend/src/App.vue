<script setup>
import PersonalInfo from './components/PersonalInfo.vue';
import WorkExperience from './components/WorkExperience.vue';
import Education from './components/Education.vue';
import Certifications from './components/Certifications.vue';
import Awards from './components/Awards.vue';
import Projects from './components/Projects.vue';
import Volunteering from './components/Volunteering.vue';
import Publications from './components/Publications.vue';
import Skills from './components/Skills.vue';
import Languages from './components/Languages.vue';
import ResumeUploader from './components/ResumeUploader.vue';
import RelevantCoursework from './components/RelevantCoursework.vue';
import { ref } from 'vue';
import api from './api';
import { useResume } from './index.js';
import Documentation from './components/Documentation.vue';
const store = useResume();
const responseMssg = ref('');
const loading = ref(false);
const validationMsg = ref('');
const showDocumentation = ref(false);

const validationSchema = {
  personalInfo: ['name', 'email', 'location', 'phone'],
  workExperiences: ['organization', 'position', 'startDate'], // example
  educations: ['instituteName', 'courseName', 'startDate'],
  certifications: ['title', 'issuingAuthority', 'issueDate'],
  awards: ['title', 'organization', 'dateEarned'],
  projects: ['title', 'date'],
  volunteering: ['organization', 'role', 'startDate'],
  publications: ['title', 'publisher', 'publishedDate'],
  skills: ['group', 'members'],
  languages: ['name', 'level'],
};

function validateSection(sectionData, requiredFields) {
  const missingFields = [];

  if (!sectionData) return missingFields;

  for (const field of requiredFields) {
    const value = sectionData[field];

    if (
      value === null ||
      value === undefined ||
      (typeof value === 'string' && value.trim() === '') ||
      (Array.isArray(value) && value.length === 0)
    ) {
      missingFields.push(field);
    }
  }

  return missingFields;
}

const checkAllSections = (validationMsg) => {
  const errors = [];

  // Validate personalInfo
  const personalInfoErrors = validateSection(
    store.$state.personalInfo,
    validationSchema.personalInfo
  );

  if (personalInfoErrors.length > 0) {
    errors.push(`Personal Info: ${personalInfoErrors.join(', ')}`);
  }

  // Validate workExperiences
  if (store.$state.workExperiences && store.$state.workExperiences.length > 0) {
    store.$state.workExperiences.forEach((item, index) => {
      const errs = validateSection(item, validationSchema.workExperiences);
      if (errs.length > 0) {
        errors.push(`Work Experience #${index + 1}: ${errs.join(', ')}`);
      }
    });
  }

  if (store.$state.educations && store.$state.educations.length > 0) {
    store.$state.educations.forEach((item, index) => {
      const errs = validateSection(item, validationSchema.educations);
      if (errs.length > 0) {
        errors.push(`Education #${index + 1}: ${errs.join(', ')}`);
      }
    });
  }

  if (store.$state.certifications && store.$state.certifications.length > 0) {
    store.$state.certifications.forEach((item, index) => {
      const errs = validateSection(item, validationSchema.certifications);
      if (errs.length > 0) {
        errors.push(`Certification #${index + 1}: ${errs.join(', ')}`);
      }
    });
  }

  if (store.$state.awards && store.$state.awards.length > 0) {
    store.$state.awards.forEach((item, index) => {
      const errs = validateSection(item, validationSchema.awards);
      if (errs.length > 0) {
        errors.push(`Award #${index + 1}: ${errs.join(', ')}`);
      }
    });
  }

  if (store.$state.projects && store.$state.projects.length > 0) {
    store.$state.projects.forEach((item, index) => {
      const errs = validateSection(item, validationSchema.projects);
      if (errs.length > 0) {
        errors.push(`Project #${index + 1}: ${errs.join(', ')}`);
      }
    });
  }

  if (store.$state.languages && store.$state.languages.length > 0) {
    store.$state.languages.forEach((item, index) => {
      const errs = validateSection(item, validationSchema.languages);
      if (errs.length > 0) {
        errors.push(`Language #${index + 1}: ${errs.join(', ')}`);
      }
    });
  }

  if (store.$state.volunteering && store.$state.volunteering.length > 0) {
    store.$state.volunteering.forEach((item, index) => {
      const errs = validateSection(item, validationSchema.volunteering);
      if (errs.length > 0) {
        errors.push(`Volunteering #${index + 1}: ${errs.join(', ')}`);
      }
    });
  }

  if (store.$state.publications && store.$state.publications.length > 0) {
    store.$state.publications.forEach((item, index) => {
      const errs = validateSection(item, validationSchema.publications);
      if (errs.length > 0) {
        errors.push(`Publication #${index + 1}: ${errs.join(', ')}`);
      }
    });
  }

  if (store.$state.skills && store.$state.skills.length > 0) {
    store.$state.skills.forEach((item, index) => {
      const errs = validateSection(item, validationSchema.skills);
      if (errs.length > 0) {
        errors.push(`Skill #${index + 1}: ${errs.join(', ')}`);
      }
    });
  }

  if (errors.length > 0) {
    // Show all errors
    validationMsg.value = errors.join('\n');
    return false;
  }
  validationMsg.value = '';
  return true;
}

function deepClean(data) {
    // If the data is null or an empty string, discard it.
    if (data === null || data === '') {
        return undefined;
    }

    // If the data is an array, iterate through its elements.
    if (Array.isArray(data)) {
        const newArray = [];
        for (let i = 0; i < data.length; i++) {
            const cleanedElement = deepClean(data[i]);
            // Only add elements that are not undefined (i.e., not null/empty string)
            if (cleanedElement !== undefined) {
                newArray.push(cleanedElement);
            }
        }
        // If the array becomes empty after cleaning, return undefined to remove it.
        return newArray.length > 0 ? newArray : undefined;
    }

    // If the data is an object, iterate through its properties.
    if (typeof data === 'object') {
        const newObject = {};
        let hasValidProperties = false;
        for (const key in data) {
            if (Object.prototype.hasOwnProperty.call(data, key)) {
                const cleanedValue = deepClean(data[key]);
                // Only add properties whose cleaned value is not undefined.
                if (cleanedValue !== undefined) {
                    newObject[key] = cleanedValue;
                    hasValidProperties = true;
                }
            }
        }
        // If the object becomes empty after cleaning, return undefined to remove it.
        return hasValidProperties ? newObject : undefined;
    }

    // If it's a primitive value (number, boolean, non-empty string), return it as is.
    return data;
}

const generateCV = async () => {
  try {
    if(checkAllSections(validationMsg)) {
      responseMssg.value = 'Generating CV...';
      loading.value = true;
      const cleanData = deepClean(JSON.parse(JSON.stringify(store.$state)));
      const response = await api.post('/generate-cv', cleanData, {headers: {'Content-Type': 'application/json'}, responseType: 'blob'});
      downloadFile(response.data, 'cv.pdf');
      responseMssg.value = 'CV generated successfully!';
    }
  } catch (error) {
    responseMssg.value = `CV generation failed: ${error}`;
  } finally { loading.value = false; }
};

const generateResume = async () => {
  try {
      if(checkAllSections(validationMsg)) {
      responseMssg.value = 'Generating Resume...';
      loading.value = true;
      const cleanData = deepClean(JSON.parse(JSON.stringify(store.$state)));
      const response = await api.post('/generate-resume', cleanData, {headers: {'Content-Type': 'application/json'}, responseType: 'blob'});
      downloadFile(response.data, 'resume.pdf');
      responseMssg.value = 'Resume generated successfully!';
    }
  } catch (error) {
    responseMssg.value = `Resume generation failed: ${error}`;
  } finally { loading.value = false; }
};
const downloadFile = (data, filename) => {
  const blob = new Blob([data], { type: 'application/pdf' });
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  a.click();
  window.URL.revokeObjectURL(url);
};

const downloadJson = () => {
  try {
    if(checkAllSections(validationMsg)) {
      responseMssg.value = 'Generating Automable JSON file...';
      loading.value = true;
      const jsonData = JSON.stringify(store.$state);
      const blob = new Blob([jsonData], { type: 'application/json' });
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url; a.download = 'resume.json'; a.click();
      window.URL.revokeObjectURL(url);
      responseMssg.value = 'Automable JSON file generated successfully!';
    }
  } catch (error) {
    responseMssg.value = `Automable JSON file generation failed: ${error}`;
  } finally { loading.value = false; }
};

const toggleView = () => {
  showDocumentation.value = !showDocumentation.value;
};
</script>

<template>
  <div class="page-wrapper">
    <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <h1 class="text-2xl font-bold mb-4">AI RESUME & CV BUILDER</h1>
      <div class="view-toggle">
        <button @click="toggleView" class="toggle-btn" :class="{ 'active': showDocumentation }">
          <span v-if="!showDocumentation">📖 view Documentation</span>
          <span v-else>🏠 Back to App</span>
        </button>
      </div>
    </div>
  </header>

  <main class="container">
    <div v-if="showDocumentation" class="documentation-wrapper"><Documentation /></div>
    <div v-else class="app-content">
      <section><PersonalInfo /></section>
      <section><RelevantCoursework /></section>
      <section><WorkExperience /></section>
      <section><Education /></section>
      <section><Certifications /></section>
      <section><Skills /></section>
      <section><Awards /></section>
      <section><Projects /></section>
      <section><Languages /></section>
      <section><Volunteering /></section>
      <section><Publications /></section>
      <section class="text-center mt-4"><p v-if="validationMsg">{{ validationMsg }}</p></section>
      <section class="form-group">
        <label for="job-description">Job Description or Target Company</label>
        <textarea
        id="job-description"
        v-model="store.jobDescription"
        class="form-control"
        placeholder="Paste the job description here for tailoring..."
        rows="4"
        ></textarea>
      </section>
      <section class="form-actions">
        <button class="btn btn-primary w-full mt-4 text-lg" @click="downloadJson">Generate JSON</button>
        <button class="btn btn-primary w-full mt-4 text-lg" @click="generateResume">Generate Resume</button>
        <button class="btn btn-secondary w-full mt-4 text-lg" @click="generateCV">Generate CV</button>
        <section class="text-center mt-4"> <div v-if="loading" class="spinner"></div> <p v-if="responseMssg">{{ responseMssg }}</p> </section>
      </section>
    <section><ResumeUploader /></section>
    </div>
  </main>
  </div>
</template>

<style scoped>

.page-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  position: static;
}

header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

.view-toggle {
  margin: 1rem;
  text-align: center;
  display: flex;
  justify-content: center;
}

.toggle-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 25px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

.toggle-btn:hover {
  transform: translateY(-2px);
  background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
  box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
}

.toggle-btn:active {
  transform: translateY(0);
  background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
  box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
}

.toggle-btn.active {
  background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
  color: white;
  box-shadow: 0 4px 15px rgba(72, 187, 120, 0.3);
}

.documentation-wrapper {
  width: 100%;
  max-width: none;
}

.app-content {
  width: 100%;
}

@media (min-width: 1024px) {
  header {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 2rem 1rem;
  }


  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}

.spinner {
  border: 4px solid rgba(0, 0, 0, 0.1);
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border-left-color: #09f;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
</style>
