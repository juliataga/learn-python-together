import streamlit as st

st.set_page_config(page_title="Cost-Tax-Tip Calculator", page_icon="🧮")

st.title("🧮 Cost - Tax - Tip Calculator")


cost = st.number_input("Total cost (₹)", min_value=0.0, step=0.50, format="%.2f")
tax_rate = st.number_input("Tax rate (%)", min_value=0.0, step=0.25, format="%.2f")
tip_percent = st.number_input("Tip percent (%)", min_value=0.0, step=0.25, format="%.2f")

if st.button("Calculate"):
    total_tax = (tax_rate / 100) * cost
    total_with_tax = cost + total_tax
    total_tip = (tip_percent / 100) * total_with_tax

    st.success("**Here’s what you’ll pay:**")
    st.write(f"• **Total without tax:** ₹{cost:,.2f}")
    st.write(f"• **Total with tax:** ₹{total_with_tax:,.2f}")
    st.write(f"• **Tip amount:** ₹{total_tip:,.2f}")

    st.balloons()  # because—we can 🎈
else:
    st.info("Enter your numbers & click **Calculate**")
