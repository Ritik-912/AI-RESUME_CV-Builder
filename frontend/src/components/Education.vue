<template>
  <section class="section-form">
    <h2 class="section-title">Education</h2>

    <div v-if="store.educations && store.educations.length">
      <div
        v-for="(edu, index) in store.educations"
        :key="index"
        class="education-entry"
      >
        <form @submit.prevent>
          <div class="form-group">
            <label :for="`institute-${index}`">Institute Name<span class="required-asterisk">*</span></label>
            <input
              :id="`institute-${index}`"
              v-model="edu.instituteName"
              type="text"
              class="form-control"
              placeholder="e.g., University of XYZ"
              required
            />
          </div>

          <div class="form-group">
            <label :for="`course-${index}`">Course Name<span class="required-asterisk">*</span></label>
            <input
              :id="`course-${index}`"
              v-model="edu.courseName"
              type="text"
              class="form-control"
              placeholder="e.g., B.Sc. in Computer Science"
              required
            />
          </div>

          <div class="form-group-inline">
            <label :for="`start-${index}`">Start Date<span class="required-asterisk">*</span></label>
            <input
              :id="`start-${index}`"
              v-model="edu.startDate"
              type="month"
              class="form-control"
              required
            />
          </div>

          <div class="form-group">
            <label :for="`end-${index}`">End Date</label>
            <input
              :id="`end-${index}`"
              v-model="edu.endDate"
              type="month"
              class="form-control"
              required
            />
          </div>

          <div class="form-group">
            <label :for="`grade-${index}`">Grade</label>
            <input
              :id="`grade-${index}`"
              v-model="edu.grade"
              type="text"
              class="form-control"
              placeholder="e.g., 3.8 GPA"
              required
            />
          </div>

          <div class="form-group full-width">
            <label :for="`desc-${index}`">Description</label>
            <textarea
              :id="`desc-${index}`"
              v-model="edu.description"
              class="form-control"
              rows="3"
              placeholder="Optional details about your studies"
            ></textarea>
          </div>
        </form>

        <div class="form-actions">
          <button
            type="button"
            class="btn btn-danger"
            @click="removeEducation(index)"
            v-if="store.educations.length > 0"
          >
            Remove
          </button>
        </div>
      </div>
    </div>
    <div v-else>
      <p>No education entries available.</p>
    </div>

    <div class="form-actions">
      <button type="button" class="btn btn-primary w-full mt-4 text-lg" @click="addEducation">
        Add Education
      </button>
    </div>
  </section>
</template>

<script setup>
import { useResume } from '../index.js';
const store = useResume();

function addEducation() {
  store.educations.push({
    instituteName: '',
    courseName: '',
    startDate: '',
    endDate: '',
    grade: '',
    description: ''
  });
}

function removeEducation(index) {
  if (store.educations.length > 0) {
    store.educations.splice(index, 1);
  }
}
</script>

<style scoped>
.education-form {
  max-width: 800px;
  margin: 2rem auto;
  padding: 1rem;
}

.education-entry {
  border: 1px solid #ccc;
  padding: 1rem;
  margin-bottom: 1.5rem;
  border-radius: 6px;
  background: #f9f9f9;
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1rem;
}

.full-width {
  grid-column: span 2;
}

.form-group label {
  font-weight: 500;
  margin-bottom: 0.5rem;
  display: block;
}

.form-control {
  width: 100%;
  padding: 0.5rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 1rem;
}

.btn {
  padding: 0.5rem 1rem;
  font-weight: 500;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-primary {
  background-color: #007bff;
  color: white;
}

.btn-primary:hover {
  background-color: #0056b3;
}

.btn-danger {
  background-color: #dc3545;
  color: white;
}

.btn-danger:hover {
  background-color: #c82333;
}

@media (max-width: 600px) {
  .full-width {
    grid-column: span 1;
  }

  .form-actions {
    flex-direction: column;
    align-items: stretch;
  }
}
</style>