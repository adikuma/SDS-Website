import streamlit as st
from streamlit_option_menu import option_menu

def main():
    st.title("Simulating the Next Generation")

    with st.sidebar:
        selected = option_menu("Navigation",
                               ["Problem Statement",
                                "Solutions",
                                "State Diagram",
                                "Solutions Simulation Result Graphs"],
                               icons=["book", "gear", "diagram-3", "graph-up"],
                               default_index=0)

    if selected == "Problem Statement":
        st.header("Problem Statement")
        # Displaying a video from the assets folder
        video_file = open('assets/video.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        
        st.subheader("Background Information")
        st.write("""
            DBS Bank is a leading financial institution with over 280 branches across 18 markets, headquartered in Singapore.
            The bank has been continually expanding its presence in China, Southeast Asia, and South Asia. The DBS Digibank
            application was created to facilitate smarter banking by allowing users to manage their finances anytime, anywhere.
        """)
        
        st.subheader("Development Bank of Singapore (DBS)")
        st.write("""
            - Founded in 1968 and has grown into a leading financial services group in Asia.
            - It is the largest local Singapore bank.
            - DBS has over 280 branches across 18 markets.
        """)
        
        st.subheader("Definition of Common Terminology")
        st.write("""
            - **Dwell Time**: Queue Time + Holding Time (if any) + Service Time.
            - **Station**: A specific area within DBS where customers interact with various service equipment such as ATMs, VTMs, and Counters.
            - **Equipment**: The array of machines or tables that are available at a particular station for customer use.
        """)
        
        st.subheader("Identification of the Common Customer Journey")
        st.write("Customers typically arrive, queue at the ATMs/VTMs, interact with the Main Queue Manager, and may utilize various services such as the ATM, VTM, Counters, or the App Booth until their needs are resolved.")
        
        st.subheader("Overarching Problems")
        st.write("""
            - Long time spent at the bank.
            - Poor allocation of resources (including manpower).
            - Unclear and contradicting information for customers.
            - Poor quality of service.
        """)
        
        st.subheader("Problem Statement")
        st.write("""
            Improving customer satisfaction is crucial, especially for DBS, as customer dwell time averages around 45 minutes. 
            This is particularly troublesome for the elderly population, who are a significant part of the clientele at certain branches. 
            Lengthy waits inconvenience customers and potentially deter them from future engagements with the bank, impacting customer retention and loyalty.
        """)
    
    elif selected == "Solutions":
        st.header("Solutions")
        st.write("This section should detail the solutions you've developed to address the problem. "
                 "You can discuss the methodologies, technologies, or algorithms employed in your solution.")
    
    elif selected == "State Diagram":
        st.header("State Diagram")
        st.write("Display the state diagram here. This diagram can illustrate the states and transitions "
                 "involved in your system or solution. You might want to include a graphical representation "
                 "if possible.")
    
    elif selected == "Solutions Simulation Result Graphs":
        st.header("Solutions Simulation Result Graphs")
        st.write("Here, you can present various graphs and visualizations that showcase the results "
                 "of simulations run as part of your solutions. These graphs can provide insights into "
                 "the effectiveness, efficiency, and performance of your proposed solutions.")

if __name__ == "__main__":
    main()
