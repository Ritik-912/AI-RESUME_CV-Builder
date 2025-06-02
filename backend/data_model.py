from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List, Optional

class PersonalInfo(BaseModel):
    name: str
    email: EmailStr
    location: str
    links: List[Optional[HttpUrl]]
    targetTitle: str
    summary: Optional[str] 

class WorkExperienceItem(BaseModel):
    organization: str
    position: str
    startDate: str
    endDate: Optional[str]
    description: Optional[str]

class EducationItem(BaseModel):
    instituteName: str
    courseName: str
    startDate: str
    endDate: Optional[str]
    grade: str
    description: Optional[str]

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
    organisation: str
    startDate: Optional[str]
    endDate: Optional[str]
    link: Optional[str]
    description: Optional[str]

class LanguageItem(BaseModel):
    name: str
    level: str

class VolunteeringItem(BaseModel):
    organization: str
    role: str
    startDate: str
    endDate: Optional[str]
    location: str
    description: Optional[str]

class PublicationItem(BaseModel):
    title: str
    publisher: str
    publishedDate: str
    abstract: Optional[str]
    link: Optional[str]

class SkillItem(BaseModel):
    name: str
    level: str

class ResumeData(BaseModel):
    personalInfo: PersonalInfo
    workExperiences: Optional[List[WorkExperienceItem]]
    educations: Optional[List[EducationItem]]
    certifications: Optional[List[CertificationItem]]
    skills: Optional[List[str]]
    awards: Optional[List[AwardItem]]
    projects: Optional[List[ProjectItem]]
    languages: Optional[List[LanguageItem]]
    volunteering: Optional[List[VolunteeringItem]]
    publications: Optional[List[PublicationItem]]
    skills: Optional[List[SkillItem]]
    jobDescription: Optional[str]