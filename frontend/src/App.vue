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
import { ref } from 'vue';
import api from './api';
import { useResume } from './index.js';
const store = useResume();
const responseMssg = ref('');
const generateCV = async () => {
  try {
    responseMssg.value = 'Generating CV...';
    console.log("Store state:", store.$state);
    console.log("Stringified payload:", JSON.stringify(store.$state, null, 2));
    const cleanData = JSON.parse(JSON.stringify(store.$state));
    console.log("Clean data:", cleanData);
    const response = await api.post('/generate-cv', cleanData, {headers: {'Content-Type': 'application/json'}, responseType: 'blob'});
    downloadFile(response.data, 'cv.pdf');
  } catch (error) {
    responseMssg.value = `CV generation failed: ${error}`;
  }
};
const generateResume = async () => {
  try {
    responseMssg.value = 'Generating Resume...';
    const response = await api.post('/generate-resume', store.$state, {responseType: 'blob'});
    downloadFile(response.data, 'resume.pdf');
  } catch (error) {
    responseMssg.value = `Resume generation failed: ${error}`;
  }
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
</script>

<template>
  <div class="page-wrapper">
    <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <h1 class="text-2xl font-bold mb-4">AI RESUME & CV BUILDER</h1>
    </div>
  </header>

  <main class="container">
    <section><PersonalInfo /></section>
    <section><WorkExperience /></section>
    <section><Education /></section>
    <section><Certifications /></section>
    <section><Skills /></section>
    <section><Awards /></section>
    <section><Projects /></section>
    <section><Languages /></section>
    <section><Volunteering /></section>
    <section><Publications /></section>
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
      <button class="btn btn-primary w-full mt-4 text-lg" @click="generateResume">Generate Resume</button>
      <button class="btn btn-secondary w-full mt-4 text-lg" @click="generateCV">Generate CV</button>
    </section>
    <section><ResumeUploader /></section>
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
</style>