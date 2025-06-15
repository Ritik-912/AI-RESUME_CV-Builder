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
        <label for="phone">Phone Number<span class="required-asterisk">*</span></label>
        <input
          id="phone"
          v-model="store.personalInfo.phone"
          type="phone"
          class="form-control"
          placeholder="+91.."
          required
        />
      </div>

      <div class="form-group">
        <label for="Linkedin">Linkedin</label>
        <input
          id="linkedin"
          v-model="store.personalInfo.linkedin"
          type="url"
          class="form-control"
          placeholder="https://www.linkedin.com/in/"
          required
        />
      </div>

      <div class="form-group">
        <label for="Github">Github</label>
        <input
          id="github"
          v-model="store.personalInfo.github"
          type="url"
          class="form-control"
          placeholder="https://github.com/"
          required
        />
      </div>
    </div>
  </section>
</template>

<script setup>
import { useResume } from '../index.js';
const store = useResume();
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