import streamlit as st
import time

# Set page configuration
st.set_page_config(page_title="Prank Simulator", page_icon="📱")

st.title("📱 WhatsApp Prank UI Simulator")
st.markdown("""
**Disclaimer:** This is a safe UI simulator built for educational purposes to learn Streamlit. 
Actual message bombing violates WhatsApp policies and will get your account permanently banned.
""")

# --- STATE MANAGEMENT ---
# Streamlit re-runs from top to bottom. We use session_state to remember if the tool is running.
if 'is_running' not in st.session_state:
    st.session_state.is_running = False

# --- UI ELEMENTS ---
st.subheader("⚙️ Target Settings")
phone_number = st.text_input("Enter Target Mobile Number (with country code):", "+91")
message = st.text_area("Message to send:", "Bhai phone utha! 🚨")

col_a, col_b = st.columns(2)
with col_a:
    count = st.number_input("Number of Messages (Loop limit):", min_value=1, max_value=500, value=10)
with col_b:
    delay = st.slider("Delay between messages (seconds):", 0.5, 5.0, 1.0)

# --- BUTTONS ---
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    # Start Button
    if st.button("🚀 Start Prank", use_container_width=True, type="primary"):
        st.session_state.is_running = True

with col2:
    # Stop Button
    if st.button("🛑 Stop Prank", use_container_width=True):
        st.session_state.is_running = False

# --- LOGIC & EXECUTION ---
if st.session_state.is_running:
    if not phone_number or not message:
        st.error("Please enter both a phone number and a message!")
        st.session_state.is_running = False
    else:
        st.info("Initiating Prank Sequence...")
        
        # UI Elements for tracking progress
        progress_bar = st.progress(0)
        status_text = st.empty()
        log_box = st.empty()
        
        logs = ""

        # The Loop
        for i in range(count):
            # Check if user clicked STOP during the loop
            if not st.session_state.is_running:
                status_text.warning("⚠️ Prank Aborted by User!")
                break
            
            # Update Progress UI
            current_msg_num = i + 1
            status_text.text(f"Sending message {current_msg_num} of {count} to {phone_number}...")
            progress_bar.progress(current_msg_num / count)
            
            # Add to logs
            logs += f"✅ [Sent] Message {current_msg_num}: '{message}' to {phone_number}\n"
            log_box.text_area("Live Terminal Logs:", logs, height=150)
            
            # Simulate the delay
            time.sleep(delay)
            
        # Completion check
        if st.session_state.is_running:
            status_text.success("🎉 Prank Loop Completed Successfully! (Simulation Finished)")
            st.session_state.is_running = False
            
elif not st.session_state.is_running and count > 0:
    st.write("System Ready. Waiting for command.")
