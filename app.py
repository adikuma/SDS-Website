import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import re

def main():
    st.set_page_config(layout="wide")
    st.markdown("""
    <h1>Simulating the Next Generation with <span style='color: #D71921;'>DBS</span></h1>
    """, unsafe_allow_html=True)
    st.markdown("---")

    with st.sidebar:
        
        selected = option_menu("Navigation",
                               ["Problem Statement",
                                "Our Solution",],
                               icons=["book", "gear", "diagram-3", "graph-up"],
                               default_index=0)

    if selected == "Problem Statement":
        st.header("Problem Statement")
        video_file = open('assets/video.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        st.write("""
            How might we effectively reduce customer dwell time for offline transactions at the DBS branches to enhance customer satisfaction?
        """)
        
        st.markdown("---")
        
        st.subheader("Background Information")
        st.write("""
            DBS Bank is a leading financial institution with over 280 branches across 18 markets, headquartered in Singapore.
            The bank has been continually expanding its presence in China, Southeast Asia, and South Asia. The DBS Digibank
            application was created to facilitate smarter banking by allowing users to manage their finances anytime, anywhere.
        """)
        st.markdown("---")
        
        st.subheader("Development Bank of Singapore (DBS)")
        st.write("""
            - Founded in 1968 and has grown into a leading financial services group in Asia.
            - It is the largest local Singapore bank.
            - DBS has over 280 branches across 18 markets.
        """)
        st.markdown("---")
        st.subheader("User Journey")
        st.image('assets/journey.png', caption='User Journey')
        st.markdown("---")
        st.subheader("Overarching Problems")
        data = {
            "Stakeholder": [
                "Customers",
                "Call Center Customer Service Officers (CSO)",
                "Queue Manager",
                "VTM-Assigned Staff"
            ],
            "Challenges": [
                "• Language barriers<br>• Conflicting information between the call centre, DBS website, and the branch",
                "• Overwhelmed by the constant updates on the DigiBank app, cannot keep track<br>• Miscommunication with branch staff causing inefficient and inaccurate services",
                "• Struggles to direct customers based on tracking live traffic conditions<br>• Will direct the customer to a different queue than what is needed",
                "• Not aware of the latest DigiBank updates<br>• Overwhelmed by the influx of customers<br>• Are required to do a 2nd card verification, causing there to be a resource intensive 1-2 staff per booth any point in time"
            ]
        }

        df = pd.DataFrame(data)

        def format_func(value):
            return value.replace("\n", "<br>")

        df['Challenges'] = df['Challenges'].apply(format_func)

        st.markdown("""
        <style>
        th {
            text-align: left;
        }
        </style>
        """, unsafe_allow_html=True)

        st.write(df.to_html(escape=False), unsafe_allow_html=True)
        st.markdown("---")
        
        st.subheader("Identification of the Common Customer Journey")
        st.write("Customers typically arrive, queue at the ATMs/VTMs, interact with the Main Queue Manager, and may utilize various services such as the ATM, VTM, Counters, or the App Booth until their needs are resolved.")
        st.markdown("---")
        st.subheader("Overarching Problems")
        st.write("""
            - Long time spent at the bank.
            - Poor allocation of resources (including manpower).
            - Unclear and contradicting information for customers.
            - Poor quality of service.
        """)
        

    
    elif selected == "Our Solution":
        st.header("Our Solution")
        st.markdown("Experience our bank simulation model here [Simulation](https://bank-simulation.netlify.app/)")

        st.write("""
        Our solution focuses on optimizing customer experience by reducing dwell times at DBS branches. By leveraging technology and improved process workflows, we aim to streamline customer interactions and minimize wait times.

        - **Enhanced Collaboration**: We've implemented a shared database for up-to-date customer information to allow for efficient and personalized service.
        - **Staff Education**: Continuous education on the latest updates to the Digibank app helps staff provide informed assistance to customers, reducing the dependency on call centers and additional verification processes.
        - **Simplified VTM Process**: We've eliminated redundancies such as the second verification step at VTMs to reduce service time.
        - **Digital Document Checklist**: A new online resource provides customers with detailed information about the documents required for various services, which can help in preparing for their bank visits ahead of time.

        This multifaceted approach ensures that every aspect of the customer journey is refined to enhance overall satisfaction and retain customer loyalty.
        """)
        
        st.image('assets/dbs.png', caption='Our Simulation App')

        st.markdown("---")
        with st.container():
            st.subheader("State Diagram")
            st.image('assets/state_diagram.jpg', caption='State Diagram of our Simulation')
        st.markdown("---")
        st.subheader("Solutions Simulation Result Graphs")
        st.write("Below are the results from our simulations showcasing the impact of our solutions:")

        st.image('assets/1.png', caption='Simulation Result 1')
        st.image('assets/2.png', caption='Simulation Result 2')
        st.image('assets/3.png', caption='Simulation Result 3')
        st.subheader("Impacts of our Solution")
        data_impacts = {
            "Solution": [
                "Central Knowledge Repository", 
                "Staff Education for the Latest Digibank Updates",
                "Simplified VTM Process through the Elimination of 2nd Verification",
                "Central Digital Document Checklist"
            ],
            "Parameter Affected in the System": [
                "Customer Arrival Rate: Reduced", 
                "Prob. of QM Requiring Assistance: Removed\nProb. of QM Handling the Issue: Increased",
                "Service Time for VTMs: Reduced\nNumber of App Booths: +1",
                "Customer Arrival Rate: Reduced\nProb. of Customer Missing Documents: Removed\nProb. of QM Requiring Assistance: Increase\nProb. of QM Handling the Issue: Increased"
            ],
            "Justification": [
                "Less customers would arrive based from inefficient instructions from the call center",
                "QMs will be informed of the latest Digibank updates and will be able to handle issues by themselves",
                "The additional time taken for the second verification in the VTMs will no longer be counted, and the staff that does these verifications can be allocated to the app booths",
                "There will be no more need for customers to re-queue from retrieving their required documents"
            ]
        }

        def colorize(text):
            replacements = {
                "Reduced": '<span style="color: yellow;">Reduced</span>',
                "Removed": '<span style="color: red;">Removed</span>',
                "\\+1": '<span style="color: green;">+1</span>',
                "Increased": '<span style="color: green;">Increased</span>',
                "Increase": '<span style="color: green;">Increase</span>'
            }

            for word, replacement in replacements.items():
                text = re.sub(word, replacement, text)
            return text

        data_impacts["Parameter Affected in the System"] = [
            colorize(text) for text in data_impacts["Parameter Affected in the System"]
        ]

        df_impacts = pd.DataFrame(data_impacts)
        html = df_impacts.to_html(escape=False)
        st.markdown(html, unsafe_allow_html=True)

        st.markdown("---")

if __name__ == "__main__":
    main()
