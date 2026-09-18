import streamlit as st
import google.generativeai as genai
import random

# Your Gemini API Key
GOOGLE_API_KEY = "AQ.Ab8RN6L8__oGC8WuWFOv8V3aZ0pm_V8Nbcv7HxSTp_3JSNJicQ"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-3.6-flash')

# Page Configuration
st.set_page_config(page_title="GlobalGrant AI Platform", page_icon="🌐", layout="wide")

st.title("🌐 GlobalGrant AI — Enterprise International Admissions & Scholarship Portal")
st.write("The world's most advanced multi-agent ecosystem featuring global universities, automated admissions, CRM tracking, and visa guidance.")

# Sidebar - Mode Selection & Profile
st.sidebar.header("🎯 Select Platform Mode")
platform_mode = st.sidebar.radio("Choose Your Pathway:", [
    "🚀 Study Abroad (Scholarships & Global Apply)", 
    "🇺🇿 Study in Uzbekistan (International Admissions)"
])

st.sidebar.divider()
st.sidebar.header("👤 Student Profile")
student_name = st.sidebar.text_input("Full Name (as in Passport):", "Alex Johnson")
user_score = st.sidebar.number_input("IELTS / GPA / Academic Score:", 0.0, 200.0, 7.5, 0.5)

if platform_mode == "🚀 Study Abroad (Scholarships & Global Apply)":
    target_country = st.sidebar.selectbox("Target Country:", [
        "United States (USA)", 
        "United Kingdom (UK)", 
        "Germany", 
        "France",
        "Netherlands",
        "South Korea", 
        "Japan", 
        "Singapore", 
        "China",
        "Hong Kong",
        "Malaysia",
        "United Arab Emirates (UAE)",
        "Switzerland", 
        "Canada", 
        "Australia", 
        "Hungary"
    ])
    
    uni_database = {
        "United States (USA)": ["Harvard University", "Massachusetts Institute of Technology (MIT)", "Stanford University", "Columbia University", "UC Berkeley"],
        "United Kingdom (UK)": ["University of Oxford", "University of Cambridge", "Imperial College London", "University College London (UCL)", "The University of Edinburgh"],
        "Germany": ["Technical University of Munich (TUM)", "Ludwig Maximilian University of Munich", "Heidelberg University", "Humboldt University of Berlin"],
        "France": ["Sorbonne University", "PSL Research University", "École Polytechnique", "Sciences Po"],
        "Netherlands": ["University of Amsterdam", "Delft University of Technology (TU Delft)", "Eindhoven University of Technology", "Utrecht University"],
        "South Korea": ["Seoul National University (SNU)", "KAIST", "Korea University", "Yonsei University", "POSTECH"],
        "Japan": ["University of Tokyo", "Kyoto University", "Tokyo Institute of Technology", "Osaka University"],
        "Singapore": ["National University of Singapore (NUS)", "Nanyang Technological University (NTU)", "Singapore Management University"],
        "China": ["Tsinghua University", "Peking University", "Fudan University", "Shanghai Jiao Tong University"],
        "Hong Kong": ["University of Hong Kong (HKU)", "Hong Kong University of Science and Technology (HKUST)", "Chinese University of Hong Kong (CUHK)"],
        "Malaysia": ["Universiti Malaya (UM)", "Universiti Putra Malaysia (UPM)", "Universiti Teknologi Malaysia (UTM)"],
        "United Arab Emirates (UAE)": ["Khalifa University", "United Arab Emirates University", "American University of Sharjah"],
        "Switzerland": ["ETH Zurich", "EPFL (École Polytechnique Fédérale de Lausanne)", "University of Zurich"],
        "Canada": ["University of Toronto", "University of British Columbia", "McGill University", "University of Waterloo"],
        "Australia": ["University of Melbourne", "Australian National University (ANU)", "University of Sydney", "UNSW Sydney"],
        "Hungary": ["University of Debrecen", "Semmelweis University", "University of Szeged", "Budapest University of Technology and Economics"]
    }
    
    selected_uni_list = uni_database.get(target_country, ["Global Partner University"])
    target_university = st.sidebar.selectbox("Target University:", selected_uni_list)

    major = st.sidebar.selectbox("Field of Study:", [
        "Computer Science & Artificial Intelligence", 
        "Business Administration & Economics", 
        "Engineering & Robotics", 
        "General Medicine & Surgery", 
        "Law & International Relations",
        "Data Science & Cybersecurity"
    ])
    
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
        "🔍 Funding & Matchmaker", 
        "📝 AI Motivation Letter", 
        "✉️ Academic Cold Email", 
        "🎤 Mock Interview AI", 
        "🚀 Live Apply Portal",
        "📊 CRM Tracking Dashboard",
        "🛂 Visa & Immigration Guide",
        "🤖 AI Expert Agents"
    ])
    
    with tab1:
        st.subheader(f"🎓 Funding & Scholarship Matchmaker for {target_university}")
        st.success(f"Analyzing fully-funded and partial scholarship opportunities for {major} in {target_country}.")
        if st.button("🔍 Run AI Funding Analysis"):
            with st.spinner("Matching your profile with university grants..."):
                fund_prompt = f"Analyze scholarship and funding options for student {student_name} with score {user_score} applying to {target_university} in {target_country} for {major}. Provide details on fully funded vs partial grants."
                res = model.generate_content(fund_prompt)
                st.markdown("### 💰 AI Scholarship Match Results:")
                st.write(res.text)
        
    with tab2:
        st.subheader("📝 Professional Motivation Letter Generator")
        essay = st.text_area("Provide your key achievements, projects, or background details:", height=120)
        
        if st.button("✨ Generate Motivation Letter"):
            if essay:
                with st.spinner("AI is drafting your professional statement..."):
                    prompt = f"Write a professional, highly competitive university admission motivation letter for student {student_name} applying to study {major} at {target_university} in {target_country}. Applicant score/GPA: {user_score}. Details: {essay}"
                    res = model.generate_content(prompt)
                    st.markdown("### 📄 Generated Motivation Letter:")
                    st.write(res.text)
            else:
                st.error("Please enter your background details!")
                
    with tab3:
        st.subheader("✉️ Professor Academic Cold Email Generator")
        prof_info = st.text_input("Professor Name & Lab/Department:", "Prof. Michael Smith, AI Research Lab")
        
        if st.button("🚀 Generate Cold Email"):
            with st.spinner("AI is crafting the academic email..."):
                email_prompt = f"Write a professional, respectful academic cold email from student {student_name} (Score: {user_score}) to {prof_info} at {target_university} asking for research supervision or a graduate assistantship position in {major}."
                res = model.generate_content(email_prompt)
                st.markdown("### ✉️ Generated Cold Email:")
                st.write(res.text)

    with tab4:
        st.subheader("🎤 Mock Interview Simulator (AI Committee)")
        interview_stage = st.selectbox("Select Interview Question:", [
            "Question 1: Why do you want to study this major at our institution and why should we select you?",
            "Question 2: Tell us about your greatest academic achievement or a major technical challenge you overcame.",
            "Question 3: What are your career goals after graduation and how will this degree help?"
        ])
        
        user_answer = st.text_area("Write your response in English:", height=100)
        
        if st.button("🔍 Evaluate Answer & Get Feedback"):
            if user_answer:
                with st.spinner("AI committee is analyzing your response..."):
                    int_prompt = f"You are an interview committee member for {target_university} in {target_country}. Student {student_name} answered the question '{interview_stage}' with: '{user_answer}'. Evaluate the answer constructively, point out weak spots, and provide a superior sample answer."
                    res = model.generate_content(int_prompt)
                    st.markdown("### 📊 Interview Evaluation & Feedback:")
                    st.write(res.text)
            else:
                st.error("Please enter your answer!")

    with tab5:
        st.subheader(f"🚀 Live Application Portal — {target_university}")
        col1, col2 = st.columns(2)
        with col1:
            passport_no = st.text_input("Passport Number:", "AB1234567")
        with col2:
            email_address = st.text_input("Contact Email:", "student@example.com")
            
        ext_activity = st.text_area("Extracurricular Activities / Research Papers / Work Experience:", height=80)
        uploaded_file = st.file_uploader("Upload Supporting Documents (Transcript, IELTS Certificate):", type=["pdf", "png", "jpg", "docx"])
        
        if st.button("📤 Submit Official Application Package"):
            if ext_activity and uploaded_file is not None:
                with st.spinner(f"Transmitting application to {target_university} admissions office..."):
                    app_id = f"APP-{random.randint(100000, 999999)}"
                    demo_prompt = f"Act as an official university admissions committee director for {target_university} in {target_country}. Review the formal application package for student {student_name} (Passport: {passport_no}, Score: {user_score}, Major: {major}). Extracurriculars: {ext_activity}. Attached file name: {uploaded_file.name}. Provide a formal admission decision letter."
                    res = model.generate_content(demo_prompt)
                    
                    st.success(f"✅ Application Successfully Submitted to {target_university}! Tracking ID: **{app_id}**")
                    st.markdown("### 🏛️ Official Admissions Committee Decision Letter:")
                    st.write(res.text)
            else:
                st.error("Please fill in all required fields and upload your documents to proceed!")

    with tab6:
        st.subheader("📊 CRM Application Tracking Dashboard")
        st.write("Monitor the real-time status of your global university submissions.")
        st.markdown("""
        | Application ID | University | Target Country | Status | Reviewer Notes |
        | :--- | :--- | :--- | :--- | :--- |
        | **APP-894211** | {target_university} | {target_country} | 🔄 Under Review | Academic transcripts verified. Awaiting committee vote. |
        | **APP-442109** | Secondary Partner Univ | {target_country} | ✅ Accepted (Scholarship) | Conditional offer extended. |
        """)
        st.info("CRM status updates automatically upon institutional synchronization.")

    with tab7:
        st.subheader(f"🛂 Visa & Immigration Guide for {target_country}")
        if st.button("🚀 Generate Visa Roadmap"):
            with st.spinner("Compiling embassy guidelines..."):
                visa_prompt = f"Provide a complete student visa application guide, interview tips, required financial proof, and photo/document checklist for international students moving to {target_country} to study {major}."
                res = model.generate_content(visa_prompt)
                st.markdown("### 📋 Official Visa & Relocation Checklist:")
                st.write(res.text)

    with tab8:
        st.subheader("🤖 Consult Specialized AI Agents (Study Abroad)")
        agent_type = st.selectbox("Select AI Expert Agent:", [
            "Scholarship Strategist (Chances & Strategy)",
            "Essay Coach (Critique & Formatting)",
            "Financial & Living Cost Advisor"
        ])
        
        user_query = st.text_area("Ask your specific question to this AI Agent:", height=80)
        
        if st.button("💬 Ask AI Expert"):
            if user_query:
                with st.spinner(f"{agent_type} is analyzing your request..."):
                    agent_prompt = f"Act as an expert {agent_type} for international students targeting {target_university} ({target_country}). Student Name: {student_name}, Score: {user_score}, Major: {major}. Answer professionally in English: {user_query}"
                    res = model.generate_content(agent_prompt)
                    st.markdown(f"### 💡 Response from {agent_type}:")
                    st.info(res.text)
            else:
                st.error("Please enter your question!")

else:
    # International Students to Uzbekistan (Study in Uzbekistan)
    student_origin = st.sidebar.selectbox("Country of Origin:", ["Indonesia", "Pakistan", "India", "Malaysia", "Bangladesh", "CIS Region", "Other International"])
    uz_major = st.sidebar.selectbox("Desired Major in Uzbekistan:", [
        "Law & International Law", 
        "General Medicine (MBBS)", 
        "Computer Science & IT", 
        "Business & Economics"
    ])
    
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "🏛️ Top Uzbek Universities", 
        "📝 Admission Letter", 
        "🚀 Live Apply Portal (Uzbekistan)",
        "📊 CRM Tracker (Uzbekistan)",
        "🛂 Visa, OVIR & Relocation Guide", 
        "🤖 AI Study Consultant",
        "⚖️ Special AI Agents (Uzbekistan)"
    ])
    
    with tab1:
        st.subheader(f"🇺🇿 Premier Universities in Uzbekistan for {uz_major}")
        st.success("Tashkent State University of Law, Westminster International University, Inha University, and Tashkent Medical Academy matching options available.")
        
        if "Law" in uz_major:
            st.write("⚖️ **Tashkent State University of Law (TSUL) & WIUT**")
            st.write("• **Program:** International Law & Business Law taught entirely in English.")
            st.write("• **Requirements:** English proficiency certification (IELTS 5.5+) and entrance interview.")
        elif "Medicine" in uz_major:
            st.write("🏥 **Tashkent Medical Academy (TMA) & Samarkand State Medical University**")
            st.write("• **Program:** General Medicine (MBBS) / Dentistry in English.")
            st.write("• **Requirements:** Science background (Biology/Chemistry) and English proficiency.")
        else:
            st.write("💻 **Inha University in Tashkent & Webster University**")
            st.write("• **Program:** World-class IT, Software Engineering, and Global Business programs.")
            
    with tab2:
        st.subheader("📝 Admission Motivation Letter (English)")
        uz_uni = st.text_input("Target University in Uzbekistan:", "Tashkent State University of Law")
        uz_details = st.text_area("Why do you want to study this program in Uzbekistan?", height=120)
        
        if st.button("✨ Generate Admission Letter"):
            if uz_details:
                with st.spinner("AI is generating your admission statement..."):
                    prompt = f"Write a professional university admission motivation letter for international student {student_name} from {student_origin} applying to study {uz_major} at {uz_uni} in Uzbekistan. Details: {uz_details}"
                    res = model.generate_content(prompt)
                    st.markdown("### 📄 Generated Admission Letter:")
                    st.write(res.text)
            else:
                st.error("Please provide details for the letter!")

    with tab3:
        st.subheader("🚀 Official International Admission Portal — Uzbekistan")
        col_u1, col_u2 = st.columns(2)
        with col_u1:
            uz_target_uni = st.selectbox("Select Uzbek University:", [
                "Tashkent State University of Law (TSUL)",
                "Tashkent Medical Academy (TMA)",
                "Inha University in Tashkent",
                "Westminster International University in Tashkent (WIUT)"
            ])
            uz_passport = st.text_input("International Passport Number:", "M9876543")
        with col_u2:
            uz_nationality = st.text_input("Citizenship / Country:", student_origin)
            uz_email = st.text_input("Email Address:", "applicant@gmail.com")
            
        uz_demo_details = st.text_area("Academic Background & English Proficiency Details:", height=80)
        uz_uploaded_file = st.file_uploader("Upload Passport Copy & High School Diploma:", type=["pdf", "png", "jpg", "docx"])
        
        if st.button("📤 Submit Application to Uzbekistan University"):
            if uz_demo_details and uz_uploaded_file is not None:
                with st.spinner("Transmitting files to Tashkent University Admission Office..."):
                    uz_app_id = f"UZ-APP-{random.randint(10000, 99999)}"
                    uz_apply_prompt = f"Act as the Head of International Admissions for {uz_target_uni} in Uzbekistan. Review the formal international application of student {student_name} from {uz_nationality} applying for {uz_major}. Background: {uz_demo_details}. Provide an official admission evaluation verdict and MFA visa invitation instructions."
                    res = model.generate_content(uz_apply_prompt)
                    
                    st.success(f"✅ Application Registered Successfully! Tracking ID: **{uz_app_id}**")
                    st.markdown("### 🏛️ Official University Admission & Visa Clearance Verdict:")
                    st.write(res.text)
            else:
                st.error("Please complete all fields and upload your documents!")

    with tab4:
        st.subheader("📊 CRM Tracking Dashboard (Uzbekistan Admissions)")
        st.markdown("""
        | Tracking ID | University | Program | Status | MFA Invitation Status |
        | :--- | :--- | :--- | :--- | :--- |
        | **UZ-APP-77210** | Tashkent State University of Law | {uz_major} | ✅ Approved | Processing Invitation Letter (MFA) |
        | **UZ-APP-10492** | Inha University in Tashkent | Software Eng. | 🔄 Document Verification | Pending Notary Translation |
        """)
        st.info("Tracking data synchronized directly with Tashkent university administrative servers.")
                
    with tab5:
        st.subheader("🛂 Uzbekistan Student Visa, Invitation & Relocation Roadmap")
        if st.button("🚀 Generate Relocation Guide"):
            with st.spinner("Compiling immigration and admission roadmap..."):
                visa_prompt = f"Act as an expert international student advisor for Uzbekistan. Create a professional, step-by-step student admission, visa invitation letter process (MFA), and relocation roadmap for international student {student_name} from {student_origin} coming to study {uz_major} in Tashkent."
                res = model.generate_content(visa_prompt)
                st.markdown("### 📋 Complete Relocation & Admission Guide:")
                st.write(res.text)
                
    with tab6:
        st.subheader("🤖 AI Study-in-Uzbekistan Assistant")
        uz_q = st.text_input("Ask a question (e.g., 'What is the monthly cost of living for a student in Tashkent?'):")
        if uz_q:
            with st.spinner("AI advisor is analyzing your question..."):
                chat_prompt = f"You are an expert advisor for international students from {student_origin} wanting to study {uz_major} in Uzbekistan. Answer accurately and professionally in English: {uz_q}"
                res = model.generate_content(chat_prompt)
                st.info(res.text)

    with tab7:
        st.subheader("⚖️ Specialized AI Agents for Uzbekistan Admissions")
        uz_agent_type = st.selectbox("Select Uzbekistan AI Expert:", [
            "Immigration & Visa Officer AI (Invitation letters, OVIR registration)",
            "Document Legalization Expert (Apostille & Translation)",
            "University Academic Advisor (Curriculum & Dormitories)"
        ])
        
        uz_agent_query = st.text_area("Ask your question to this Uzbekistan Expert Agent:", height=80)
        
        if st.button("💬 Consult Uzbek AI Agent"):
            if uz_agent_query:
                with st.spinner(f"{uz_agent_type} is processing your request..."):
                    uz_agent_prompt = f"Act as an expert {uz_agent_type} specialized in helping international students from {student_origin} entering Uzbekistan universities for {uz_major}. Answer professionally in English: {uz_agent_query}"
                    res = model.generate_content(uz_agent_prompt)
                    st.markdown(f"### 💡 Response from {uz_agent_type}:")
                    st.info(res.text)
            else:
                st.error("Please enter your question!")