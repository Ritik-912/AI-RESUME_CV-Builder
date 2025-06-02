<template>
  <section class="section-form">
    <h2>Certifications</h2>

    <div v-if="store.certifications && store.certifications.length">
      <div
        v-for="(cert, index) in store.certifications"
        :key="index"
        class="cert-entry"
      >
        <form @submit.prevent>
          <div class="form-group">
            <label :for="`cert-title-${index}`">Certification Title</label>
            <input
              :id="`cert-title-${index}`"
              v-model="cert.title"
              type="text"
              class="form-control"
              placeholder="e.g., AWS Certified Solutions Architect"
              required
            />
          </div>

          <div class="form-group">
            <label :for="`cert-issuer-${index}`">Issuing Authority</label>
            <input
              :id="`cert-issuer-${index}`"
              v-model="cert.issuingAuthority"
              type="text"
              class="form-control"
              placeholder="e.g., Amazon Web Services"
              required
            />
          </div>

          <div class="form-group">
            <label :for="`cert-date-${index}`">Issue Date</label>
            <input
              :id="`cert-date-${index}`"
              v-model="cert.issueDate"
              type="month"
              class="form-control"
              required
            />
          </div>
        </form>

        <div class="form-actions">
          <button
            type="button"
            class="btn btn-danger"
            @click="removeCertification(index)"
            v-if="store.certifications.length > 1"
          >
            Remove
          </button>
        </div>
      </div>
    </div>
    <div v-else>
      <p>No certifications available.</p>
    </div>

    <div class="form-actions">
      <button type="button" class="btn btn-primary w-full mt-4 text-lg" @click="addCertification">
        Add Certification
      </button>
    </div>
  </section>
</template>

<script setup>
import { onMounted } from 'vue';
import { useResume } from '../index.js';
const store = useResume();

function addCertification() {
  store.certifications.push({
    title: '',
    issuingAuthority: '',
    issueDate: ''
  });
}

function removeCertification(index) {
  store.certifications.splice(index, 1);
}

onMounted(() => {
  if (!store.certifications || store.certifications.length === 0) {
    store.certifications = [{
      title: '',
      issuingAuthority: '',
      issueDate: ''
    }];
  }
});
</script>

<style scoped>

.cert-entry {
  border: 1px solid #ccc;
  padding: 1rem;
  margin-bottom: 1.5rem;
  border-radius: 6px;
  background: #f9f9f9;
}

@media (max-width: 600px) {
  .form-actions {
    flex-direction: column;
    align-items: stretch;
  }
}
</style>