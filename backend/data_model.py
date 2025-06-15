from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List, Optional

class PersonalInfo(BaseModel):
    name: str
    phone: str
    email: EmailStr
    location: str
    linkedin: Optional[HttpUrl] | None = None
    github: Optional[HttpUrl] | None = None

class WorkExperienceItem(BaseModel):
    organization: str
    position: str
    startDate: str
    endDate: Optional[str] | None = None
    description: Optional[str] | None = None
    location: Optional[str] | None = None

class EducationItem(BaseModel):
    instituteName: str
    courseName: str
    startDate: str
    endDate: Optional[str] | None = None
    grade: Optional[str] | None = None
    location: Optional[str] | None = None

class CertificationItem(BaseModel):
    title: str
    issuingAuthority: str
    issueDate: str

class AwardItem(BaseModel):
    title: str
    organization: str
    dateEarned: str

class ProjectItem(BaseModel):
    title: str
    date: str
    link: Optional[HttpUrl] | None = None
    description: Optional[str] | None = None
    techStack: Optional[str] | None = None

class VolunteeringItem(BaseModel):
    organization: str
    role: str
    startDate: str
    endDate: Optional[str] | None = None
    location: str
    description: Optional[str] | None = None

class PublicationItem(BaseModel):
    title: str
    publisher: str
    publishedDate: str
    abstract: Optional[str] | None = None
    link: Optional[HttpUrl] | None = None

class SkillItem(BaseModel):
    name: str
    level: str

class SkillGroup(BaseModel):
    group: str
    members: List[SkillItem]

class LanguageItem(BaseModel):
    name: str
    level: str

class ResumeData(BaseModel):
    personalInfo: PersonalInfo
    relevantCoursework: Optional[List[str]] | None = None
    workExperiences: Optional[List[WorkExperienceItem]] | None = None
    educations: Optional[List[EducationItem]] | None = None
    certifications: Optional[List[CertificationItem]] | None = None
    skills: Optional[List[SkillGroup]] | None = None
    awards: Optional[List[AwardItem]] | None = None
    projects: Optional[List[ProjectItem]] | None = None
    volunteering: Optional[List[VolunteeringItem]] | None = None
    publications: Optional[List[PublicationItem]] | None = None
    languages: Optional[List[LanguageItem]] | None = None
    jobDescription: Optional[str] | None = None