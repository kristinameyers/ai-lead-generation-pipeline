"""
Agentic Lead Gen & Enrichment Pipeline - UI Panel
Author: Senior AI Solutions Architect
Description: Web interface wrapping sequential multi-agent execution frames
             to input raw metadata and isolate deep profile generations.
"""

import streamlit as st
import os
from enrichment_agent import LeadEnrichmentPipeline

# --- INITIAL WINDOW DECORATION ---
st.set_page_config(page_title="Agentic Lead Intel Engine", page_icon="🎯", layout="wide")

st.title("🎯 Agentic Lead Gen & Enrichment Workspace")
st.caption("Sequential Multi-Agent Pipeline for Precision Account Intelligence & Personalized Outreach")
st.markdown("---")

# --- CENTRAL CONTROL PANEL SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Configuration Hub")
    st.markdown("### 🔑 Authentication")
    st.caption("Supply your Google AI Studio API key. The app leverages the modern `google-genai` engine framework.")
    user_api_key = st.text_input("Gemini API Key", type="password")
    
    st.markdown("---")
    if st.button("♻️ Clear Pipeline Variables", use_container_width=True):
        st.session_state.clear()
        st.rerun()

# --- MAIN SCREEN VIEWPORT ---
col_controls, col_display = st.columns([1, 1.2], gap="large")

with col_controls:
    st.markdown("### 1. Ingest Prospect Target Data")
    st.caption("Input baseline business metrics extracted from CRMs, LinkedIn profiles, or search fragments.")
    
    with st.form("prospect_form"):
        form_name = st.text_input("Prospect Executive Name", value="Marcus")
        form_role = st.text_input("Target Corporate Role / Title", value="VP of Delivery Services")
        
        c_col, d_col = st.columns(2)
        with c_col:
            form_company = st.text_input("Company Name", value="Vanguard Cloud Solved")
        with d_col:
            form_domain = st.text_input("Corporate Domain URL", value="vanguardcloudsolved.com")
            
        form_notes = st.text_area(
            "Raw Scraped Context / Unstructured Text Logs",
            value=(
                "Salesforce boutique partner focusing on migration implementations. Growing fast but struggling "
                "to scale internal engineering benches. Mentioned on an interview last week that they are losing "
                "mid-market deals because their delivery timelines are stretching to 12 weeks."
            ),
            height=150
        )
        
        submit_btn = st.form_submit_button("🚀 Activate Multi-Agent Execution Loop", use_container_width=True)

with col_display:
    st.markdown("### 2. Multi-Agent Sequential Workspace Logs")
    
    if submit_btn or st.session_state.get("pipeline_triggered", False):
        if not user_api_key:
            st.error("🔑 Access Denied: Please input a valid Gemini API Key in the sidebar control panel.")
        else:
            if submit_btn:
                st.session_state["pipeline_triggered"] = True
                
                # Instantiate your core engine block from enrichment_agent.py
                with st.spinner("Initializing Agent Subsystems..."):
                    engine = LeadEnrichmentPipeline(api_key=user_api_key)
                
                # Execute the sequence passing text state down the pipe
                with st.spinner("Executing sequence tracks (Passing state downstream)..."):
                    results = engine.execute_pipeline(
                        contact_name=form_name,
                        company_name=form_company,
                        domain=form_domain,
                        role=form_role,
                        raw_notes=form_notes
                    )
                    st.session_state["pipeline_results"] = results
            
            # Extract computed state artifacts from session variables
            output_data = st.session_state.get("pipeline_results", {})
            
            st.success("✨ Multi-Agent orchestration loops finalized! Review outputs across roles below:")
            
            # Render specialized structural tabs isolating individual agent outputs
            tab_intel, tab_pain, tab_copy = st.tabs([
                "🕵️ Agent 1: Corporate Intelligence", 
                "📐 Agent 2: Persona Architect", 
                "✍️ Agent 3: B2B Copywriter"
            ])
            
            with tab_intel:
                st.markdown("#### **Extracted Corporate Positioning Profile**")
                st.info("Role Target: Corporate Fact Extraction Sub-Agent")
                st.code(output_data.get("company_profile", ""), language="text")
                
            with tab_pain:
                st.markdown("#### **Diagnosed Executive Operational Headaches**")
                st.info("Role Target: Strategic Persona Bottleneck Consultant")
                st.code(output_data.get("pain_points", ""), language="text")
                
            with tab_copy:
                st.markdown("#### **Bespoke Personalization Outreach Email**")
                st.info("Role Target: Conversion-Optimized B2B Copywriter")
                st.text_area(
                    "Generated Sequence Output (Editable Asset)", 
                    value=output_data.get("outreach_email", ""), 
                    height=250
                )
    else:
        st.info("Populate target prospect variables on the left pane and trigger the pipeline execution loop.")