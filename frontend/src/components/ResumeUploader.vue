<template>
  <div class="mt-8">
    <h2 class="text-xl font-semibold">Upload Existing CV</h2>
    <input
      type="file"
      accept=".pdf,.doc,.docx,.txt"
      @change="handleUpload"
      ref="fileInput"
    />
    <p v-if="errorMsg" class="error-message">{{ errorMsg }}</p>
    <p v-if="successMsg" class="success-message">{{ successMsg }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useResume } from '../index.js';

const store = useResume();
const fileInput = ref(null);
const errorMsg = ref('');
const successMsg = ref('');

const handleUpload = (event) => {
  errorMsg.value = '';
  successMsg.value = '';

  const file = event.target.files[0];
  if (!file) {
    errorMsg.value = 'No file selected.';
    return;
  }

  const reader = new FileReader();
  reader.onload = async () => {
    try {
      const base64 = reader.result.split(',')[1];
      const response = await fetch('/extract-data', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ file: base64 }),
      });

      if (!response.ok) {
        throw new Error('Failed to extract data from file');
      }

      const data = await response.json();
      Object.assign(store, data);
      successMsg.value = 'Resume uploaded and data extracted successfully!';
      // Clear the file input so the same file can be uploaded again if needed
      if (fileInput.value) fileInput.value.value = '';
    } catch (error) {
      errorMsg.value = error.message || 'An unexpected error occurred.';
    }
  };

  reader.onerror = () => {
    errorMsg.value = 'Failed to read the file.';
  };

  reader.readAsDataURL(file);
};
</script>

<style scoped>
.mt-8 {
  margin-top: 2rem;
}
.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}
.font-semibold {
  font-weight: 600;
}
.error-message {
  margin-top: 1rem;
  color: #dc3545;
}
.success-message {
  margin-top: 1rem;
  color: #28a745;
}
</style>