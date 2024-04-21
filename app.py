import streamlit as st
from streamlit_option_menu import option_menu

def main():

    # st.title("Simulating the Next Generation")

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
            Improving customer satisfaction is crucial, especially for DBS, as customer dwell time averages around 45 minutes. 
            This is particularly troublesome for the elderly population, who are a significant part of the clientele at certain branches. 
            Lengthy waits inconvenience customers and potentially deter them from future engagements with the bank, impacting customer retention and loyalty.
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
        
        st.subheader("Definition of Common Terminology")
        st.write("""
            - **Dwell Time**: Queue Time + Holding Time (if any) + Service Time.
            - **Station**: A specific area within DBS where customers interact with various service equipment such as ATMs, VTMs, and Counters.
            - **Equipment**: The array of machines or tables that are available at a particular station for customer use.
        """)
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
        st.markdown("---")
        with st.container():
            st.subheader("State Diagram")
            st.image('assets/state_diagram.jpg', caption='State Diagram')
        st.markdown("---")
        with st.container():
            st.subheader("Solutions Simulation Result Graphs")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image('assets/1.png', caption='Simulation Result 1')
            with col2:
                st.image('assets/2.png', caption='Simulation Result 2')
            with col3:
                st.image('assets/3.png', caption='Simulation Result 3')

if __name__ == "__main__":
    main()
