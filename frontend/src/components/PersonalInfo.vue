<template>
  <section class="section-form">
    <h2 class="section-title">Personal Information</h2>

    <div class="form-grid">
      <div class="form-group">
        <label for="name">Name<span class="required-asterisk">*</span></label>
        <input
          id="name"
          v-model="store.personalInfo.name"
          type="text"
          class="form-control"
          placeholder="Full Name"
          required
        />
      </div>

      <div class="form-group">
        <label for="email">Email<span class="required-asterisk">*</span></label>
        <input
          id="email"
          v-model="store.personalInfo.email"
          type="email"
          class="form-control"
          placeholder="Email Address"
          required
        />
      </div>

      <div class="form-group">
        <label for="location">Location<span class="required-asterisk">*</span></label>
        <input
          id="location"
          v-model="store.personalInfo.location"
          type="text"
          class="form-control"
          placeholder="City, Country"
          required
        />
      </div>

      <div class="form-group">
        <label for="links">Portfolio / LinkedIn</label>
        <div v-for="(link, index) in store.personalInfo.links" :key="index">
          <span class="required-asterisk">*</span>
          <input
          :id="`linkText-${index}`"
          v-model="store.personalInfo.links[index].text"
          type="text"
          class="form-control"
          placeholder="Display Name"><span class="required-asterisk">*</span>
          <input
          :id="`link-${index}`"
          v-model="store.personalInfo.links[index].url"
          type="url"
          class="form-control"
          placeholder="https://..."
        />
        <button type="button" @click="removeLink(index)" class="btn-danger">Remove link</button>
        </div>
        <button type="button" @click="addLink" class="btn-success">Add Link</button>
      </div>

      <div class="form-group">
        <label for="targetTitle">Target Job Title</label>
        <input
          id="targetTitle"
          v-model="store.personalInfo.targetTitle"
          type="text"
          class="form-control"
          placeholder="e.g. Frontend Developer"
          required
        />
      </div>

      <div class="form-group full-width">
        <label for="summary">Professional Summary</label>
        <textarea
          id="summary"
          v-model="store.personalInfo.summary"
          class="form-control"
          placeholder="A concise summary of your background and career goals..."
          rows="4"
        ></textarea>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useResume } from '../index.js';
const store = useResume();
const addLink = () => {
  store.personalInfo.links.push({text: '', url: ''});
};
const removeLink = (index) => {
  store.personalInfo.links.splice(index, 1);
};
</script>

<style scoped>
.form-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.25rem;
}

.form-group label {
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.form-control {
  width: 100%;
  padding: 0.5rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.full-width {
  grid-column: span 2;
}

@media (max-width: 600px) {
  .full-width {
    grid-column: span 1;
  }
}
</style>