"""
Agentic Lead Gen & Enrichment Pipeline - Core Engine
Author: Senior AI Solutions Architect
Description: Modular sequential multi-agent pipeline using the native Google GenAI SDK 
             to automate B2B company research, persona mapping, and personalized outreach.
"""

import os
import json
from google import genai
from google.genai import types

class LeadEnrichmentPipeline:
    def __init__(self, api_key: str):
        """Initializes the centralized Gemini client."""
        self.client = genai.Client(api_key=api_key)
        self.model_name = 'gemini-2.5-flash'

    def run_company_researcher(self, company_name: str, domain: str, raw_context: str) -> str:
        """Agent 1: Extracts corporate positioning, value props, and core data points."""
        system_instruction = (
            "You are an expert Corporate Intelligence Agent. Your goal is to analyze raw company data, "
            "web fragments, or descriptions, and distill them into a structured corporate profile. "
            "Focus on: 1. Core Value Proposition, 2. Target Monetization Model, 3. Notable Scale/Milestones. "
            "Be factual, concise, and eliminate corporate buzzword fluff."
        )
        
        prompt = f"Analyze this target entity: Co Name: {company_name} | Website: {domain}. Context: {raw_context}"
        
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.2
            )
        )
        return response.text

    def run_persona_architect(self, company_profile: str, target_role: str) -> str:
        """Agent 2: Maps corporate profiles to specific executive buyer pain points."""
        system_instruction = (
            f"You are a B2B Buyer Persona Architect specializing in targeting {target_role} executives. "
            "Given a target company profile, diagnose the top 2 operational headaches, resource constraints, "
            "or technical bottlenecks this specific executive is likely facing right now within their organization."
        )
        
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=f"Analyze this company profile and map executive friction points:\n\n{company_profile}",
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.3
            )
        )
        return response.text

    def run_outreach_copywriter(self, client_name: str, company_name: str, profile: str, pain_points: str) -> str:
        """Agent 3: Compiles intelligence and friction logs into a highly tailored email asset."""
        system_instruction = (
            "You are an elite B2B Copywriter. You write highly conversion-optimized, low-pressure cold outreach. "
            "CRITICAL RULES:\n"
            "- Never say 'I hope this email finds you well' or use generic automated introductions.\n"
            "- Keep the entire email under 120 words.\n"
            "- Reference their specific company positioning and identified operational pain points naturally.\n"
            "- End with a soft, zero-pressure call to action (e.g., 'Open to a brief sync next Tuesday?')."
        )
        
        prompt = (
            f"Write a hyper-personalized outreach email to {client_name} at {company_name}.\n\n"
            f"Company Intelligence Intel:\n{profile}\n\n"
            f"Target Executive Pain Points:\n{pain_points}"
        )
        
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.5
            )
        )
        return response.text

    def execute_pipeline(self, contact_name: str, company_name: str, domain: str, role: str, raw_notes: str):
        """Coordinates the sequential execution loop passing state tokens downwards."""
        print(f"🚀 Initializing Agentic Pipeline for {company_name}...")
        
        # Step 1: Corporate Intelligence Gathering
        company_intel = self.run_company_researcher(company_name, domain, raw_notes)
        print("✅ Step 1: Corporate Intelligence Profile Compiled.")
        
        # Step 2: Persona Friction Analysis
        persona_intel = self.run_persona_architect(company_intel, role)
        print(f"✅ Step 2: Operational Friction Mapped for role: {role}.")
        
        # Step 3: Hyper-Personalized Asset Generation
        final_email = self.run_outreach_copywriter(contact_name, company_name, company_intel, persona_intel)
        print("✅ Step 3: Bespoke Outreach Copy Sequenced Successfully.")
        
        return {
            "company_profile": company_intel,
            "pain_points": persona_intel,
            "outreach_email": final_email
        }

# --- LOCAL SANDBOX RUNNER ---
if __name__ == "__main__":
    # Pull native key from environment or drop string here for quick verification testing
    API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY")
    
    if API_KEY == "YOUR_GEMINI_API_KEY":
        print("⚠️ Please replace placeholder with your live Gemini API key to test the execution loops.")
    else:
        # Fictional noisy input data mimicking a scraped web snippet or raw CRM note
        test_notes = (
            "Salesforce boutique partner focusing on migration implementations. Growing fast but struggling "
            "to scale internal engineering benches. Mentioned on an interview last week that they are losing "
            "mid-market deals because their delivery timelines are stretching to 12 weeks."
        )
        
        pipeline = LeadEnrichmentPipeline(api_key=API_KEY)
        results = pipeline.execute_pipeline(
            contact_name="Marcus",
            company_name="Vanguard Cloud Solved",
            domain="vanguardcloudsolved.example.com",
            role="VP of Delivery Services",
            raw_notes=test_notes
        )
        
        print("\n" + "="*50 + "\n🔥 PIPELINE GENERATION OUTPUT\n" + "="*50)
        print(f"\n📧 TAILORED OUTREACH EMAIL:\n\n{results['outreach_email']}")