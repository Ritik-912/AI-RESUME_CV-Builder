import { defineStore } from "pinia";
export const useResume = defineStore("resume", {
  state: () => ({
    personalInfo: {
      name: '',
      email: '',
      location: '',
      links: [],
      targetTitle: '',
      summary: '',
    },
    workExperiences: [],
    educations: [],
    certifications: [],
    awards: [],
    projects: [],
    volunteering: [],
    publications: [],
    languages: [],
    skills: [],
    jobDescription: '',
  }),
});