import streamlit as st

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="Chinaka Enterprises",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

    .stApp {
        background-color: #fffaf3;
    }

    .main-title {
        font-size: 55px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0;
        color: #5b2c06;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #765c42;
        margin-bottom: 30px;
    }

    .hero {
        padding: 50px;
        border-radius: 20px;
        background: linear-gradient(
            135deg,
            #7b3f00,
            #c98a18,
            #f2d388
        );
        color: white;
        text-align: center;
        margin-bottom: 35px;
    }

    .hero h1 {
        font-size: 48px;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 20px;
    }

    .product-card {
        background-color: white;
        padding: 18px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        min-height: 380px;
    }

    .product-name {
        font-size: 23px;
        font-weight: bold;
        color: #5b2c06;
    }

    .price {
        font-size: 21px;
        font-weight: bold;
        color: #9a5b00;
    }

    .category {
        color: #8a735d;
        font-size: 14px;
    }

    .section-title {
        color: #5b2c06;
        font-size: 35px;
        font-weight: bold;
        margin-top: 25px;
    }

    .footer {
        text-align: center;
        padding: 30px;
        margin-top: 50px;
        background-color: #3e2008;
        color: white;
        border-radius: 15px;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------
# PRODUCT DATA
# -----------------------------
products = [
    {
        "id": 1,
        "name": "Ankara Print Dress",
        "category": "African Clothing",
        "price": 65.00,
        "image": "https://images.unsplash.com/photo-1591369822096-ffd140ec948f",
        "description": "Beautiful African-inspired Ankara print dress."
    },
    {
        "id": 2,
        "name": "African Print Shirt",
        "category": "African Clothing",
        "price": 45.00,
        "image": "https://images.unsplash.com/photo-1594938298603-c8148c4dae35",
        "description": "Stylish African print shirt for everyday wear."
    },
    {
        "id": 3,
        "name": "Kente Inspired Outfit",
        "category": "African Clothing",
        "price": 85.00,
        "image": "https://images.unsplash.com/photo-1583743814966-8936f37f4a6a",
        "description": "Colorful Kente-inspired outfit with bold patterns."
    },
    {
        "id": 4,
        "name": "African Headwrap",
        "category": "Accessories",
        "price": 25.00,
        "image": "https://images.unsplash.com/photo-1581044777550-4cfa60707c03",
        "description": "Versatile headwrap featuring vibrant African patterns."
    },
    {
        "id": 5,
        "name": "Raw Shea Butter",
        "category": "Shea Butter",
        "price": 15.00,
        "image": "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b",
        "description": "Rich, natural shea butter for skin and hair care."
    },
    {
        "id": 6,
        "name": "Shea Butter Body Cream",
        "category": "Shea Butter",
        "price": 18.00,
        "image": "https://images.unsplash.com/photo-1611930022073-b7a4ba5fcccd",
        "description": "Moisturizing body cream made with shea butter."
    },
    {
        "id": 7,
        "name": "Shea Butter Hair Cream",
        "category": "Shea Butter",
        "price": 17.00,
        "image": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e",
        "description": "Nourishing hair cream formulated with shea butter."
    },
    {
        "id": 8,
        "name": "Shea Butter Gift Set",
        "category": "Gift Sets",
        "price": 35.00,
        "image": "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108",
        "description": "A beautiful gift set featuring shea butter products."
    }
]


# -----------------------------
# SESSION STATE
# -----------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []


# -----------------------------
# FUNCTIONS
# -----------------------------
def add_to_cart(product):
    st.session_state.cart.append(product)


def remove_from_cart(index):
    st.session_state.cart.pop(index)


def cart_total():
    return sum(item["price"] for item in st.session_state.cart)


# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🌍 Chinaka Enterprises")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Shop",
        "African Clothing",
        "Shea Butter",
        "Shopping Cart",
        "Checkout",
        "About Us"
    ]
)

st.sidebar.markdown("---")

st.sidebar.write(
    f"🛒 Cart Items: **{len(st.session_state.cart)}**"
)

st.sidebar.markdown("---")

st.sidebar.info(
    "Celebrating African fashion, beauty, culture, and craftsmanship."
)


# -----------------------------
# HOME PAGE
# -----------------------------
if page == "Home":

    st.markdown("""
    <div class="hero">
        <h1>🌍 Chinaka Enterprises</h1>
        <p>
        African Fashion • Natural Shea Butter • Culture
        </p>
        <p>
        Bringing African-inspired fashion and natural beauty products
        to your doorstep.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Shop Our Collections</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 👗 African Clothing")
        st.write(
            "Discover vibrant African-inspired clothing designed "
            "to celebrate culture and individuality."
        )
        if st.button("Shop Clothing"):
            st.session_state["navigate"] = "African Clothing"
            st.rerun()

    with col2:
        st.markdown("### 🧴 Shea Butter")
        st.write(
            "Explore rich, moisturizing shea butter products "
            "for your skin and hair."
        )
        if st.button("Shop Shea Butter"):
            st.session_state["navigate"] = "Shea Butter"
            st.rerun()

    with col3:
        st.markdown("### 🎁 Gift Sets")
        st.write(
            "Give something meaningful with our collection "
            "of African-inspired gifts."
        )
        if st.button("View Gift Sets"):
            st.session_state["navigate"] = "Shop"
            st.rerun()

    st.markdown("---")

    st.markdown(
        '<div class="section-title">Featured Products</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(4)

    for i, product in enumerate(products[:4]):
        with cols[i]:
            st.image(product["image"], use_container_width=True)

            st.markdown(
                f'<div class="product-name">{product["name"]}</div>',
                unsafe_allow_html=True
            )

            st.write(product["description"])

            st.markdown(
                f'<div class="price">${product["price"]:.2f}</div>',
                unsafe_allow_html=True
            )

            if st.button(
                "Add to Cart",
                key=f"home_{product['id']}"
            ):
                add_to_cart(product)
                st.success("Added to cart!")


# -----------------------------
# SHOP PAGE
# -----------------------------
elif page == "Shop":

    st.markdown(
        '<div class="section-title">🛍️ Shop Chinaka Enterprises</div>',
        unsafe_allow_html=True
    )

    search = st.text_input(
        "🔎 Search products",
        placeholder="Search clothing, shea butter..."
    )

    filtered_products = products

    if search:
        filtered_products = [
            p for p in products
            if search.lower() in p["name"].lower()
            or search.lower() in p["category"].lower()
        ]

    cols = st.columns(4)

    for i, product in enumerate(filtered_products):

        with cols[i % 4]:

            st.image(
                product["image"],
                use_container_width=True
            )

            st.markdown(
                f'<div class="product-name">{product["name"]}</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="category">{product["category"]}</div>',
                unsafe_allow_html=True
            )

            st.write(product["description"])

            st.markdown(
                f'<div class="price">${product["price"]:.2f}</div>',
                unsafe_allow_html=True
            )

            if st.button(
                "🛒 Add to Cart",
                key=f"shop_{product['id']}"
            ):
                add_to_cart(product)
                st.success(
                    f"{product['name']} added!"
                )


# -----------------------------
# CLOTHING PAGE
# -----------------------------
elif page == "African Clothing":

    st.markdown(
        '<div class="section-title">👗 African Clothing</div>',
        unsafe_allow_html=True
    )

    clothing = [
        p for p in products
        if p["category"] == "African Clothing"
        or p["category"] == "Accessories"
    ]

    cols = st.columns(3)

    for i, product in enumerate(clothing):

        with cols[i % 3]:

            st.image(
                product["image"],
                use_container_width=True
            )

            st.markdown(
                f'<div class="product-name">{product["name"]}</div>',
                unsafe_allow_html=True
            )

            st.write(product["description"])

            st.markdown(
                f'<div class="price">${product["price"]:.2f}</div>',
                unsafe_allow_html=True
            )

            if st.button(
                "Add to Cart",
                key=f"clothing_{product['id']}"
            ):
                add_to_cart(product)
                st.success("Added to cart!")


# -----------------------------
# SHEA BUTTER PAGE
# -----------------------------
elif page == "Shea Butter":

    st.markdown(
        '<div class="section-title">🧴 Shea Butter Collection</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Nourish your skin and hair with our shea butter collection."
    )

    shea_products = [
        p for p in products
        if p["category"] == "Shea Butter"
        or p["category"] == "Gift Sets"
    ]

    cols = st.columns(3)

    for i, product in enumerate(shea_products):

        with cols[i % 3]:

            st.image(
                product["image"],
                use_container_width=True
            )

            st.markdown(
                f'<div class="product-name">{product["name"]}</div>',
                unsafe_allow_html=True
            )

            st.write(product["description"])

            st.markdown(
                f'<div class="price">${product["price"]:.2f}</div>',
                unsafe_allow_html=True
            )

            if st.button(
                "Add to Cart",
                key=f"shea_{product['id']}"
            ):
                add_to_cart(product)
                st.success("Added to cart!")


# -----------------------------
# SHOPPING CART
# -----------------------------
elif page == "Shopping Cart":

    st.markdown(
        '<div class="section-title">🛒 Your Shopping Cart</div>',
        unsafe_allow_html=True
    )

    if not st.session_state.cart:

        st.info(
            "Your cart is empty. Start shopping to add products!"
        )

    else:

        for i, item in enumerate(st.session_state.cart):

            col1, col2, col3 = st.columns([2, 4, 2])

            with col1:
                st.image(
                    item["image"],
                    width=120
                )

            with col2:
                st.subheader(item["name"])
                st.write(item["category"])

            with col3:
                st.write(
                    f"**${item['price']:.2f}**"
                )

                if st.button(
                    "Remove",
                    key=f"remove_{i}"
                ):
                    remove_from_cart(i)
                    st.rerun()

        st.markdown("---")

        subtotal = cart_total()
        shipping = 7.99 if subtotal > 0 else 0
        total = subtotal + shipping

        st.write(f"Subtotal: **${subtotal:.2f}**")
        st.write(f"Shipping: **${shipping:.2f}**")

        st.markdown(
            f"### Total: ${total:.2f}"
        )

        if st.button("Proceed to Checkout"):
            st.info(
                "Select Checkout from the sidebar."
            )


# -----------------------------
# CHECKOUT
# -----------------------------
elif page == "Checkout":

    st.markdown(
        '<div class="section-title">💳 Checkout</div>',
        unsafe_allow_html=True
    )

    if not st.session_state.cart:

        st.warning(
            "Your cart is empty. Add products before checking out."
        )

    else:

        subtotal = cart_total()
        shipping = 7.99
        total = subtotal + shipping

        st.subheader("Order Summary")

        for item in st.session_state.cart:
            st.write(
                f"{item['name']} — ${item['price']:.2f}"
            )

        st.markdown("---")

        st.write(f"Subtotal: ${subtotal:.2f}")
        st.write(f"Shipping: ${shipping:.2f}")
        st.write(f"**Total: ${total:.2f}**")

        st.markdown("---")

        st.subheader("Customer Information")

        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")

        address = st.text_area(
            "Shipping Address"
        )

        city = st.text_input("City")
        state = st.text_input("State")
        zip_code = st.text_input("ZIP Code")

        st.subheader("Payment")

        payment = st.selectbox(
            "Payment Method",
            [
                "Credit/Debit Card",
                "PayPal",
                "Cash App"
            ]
        )

        if st.button(
            "Place Order",
            type="primary"
        ):

            if (
                name
                and email
                and address
                and city
                and state
                and zip_code
            ):

                st.success(
                    f"Thank you, {name}! "
                    "Your Chinaka Enterprises order has been received."
                )

                st.balloons()

                st.session_state.cart = []

            else:

                st.error(
                    "Please complete all required shipping information."
                )


# -----------------------------
# ABOUT PAGE
# -----------------------------
elif page == "About Us":

    st.markdown(
        '<div class="section-title">🌍 About Chinaka Enterprises</div>',
        unsafe_allow_html=True
    )

    st.write("""
    ### Our Story

    Chinaka Enterprises celebrates African culture through fashion,
    beauty, and natural products.

    Our goal is to connect customers with beautiful African-inspired
    clothing and high-quality shea butter products.

    ### What We Offer

    👗 African-inspired clothing

    🧴 Natural shea butter products

    🎁 Gift sets

    🌍 Culture-inspired products

    ### Our Mission

    To provide customers with products that celebrate African
    culture, creativity, craftsmanship, and natural beauty.
    """)

    st.markdown("---")

    st.subheader("📩 Contact Us")

    st.write(
        "Email: chinakaenterprises@example.com"
    )

    st.write(
        "Phone: (555) 123-4567"
    )


# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
<div class="footer">
    <h3>🌍 Chinaka Enterprises</h3>
    <p>African Fashion • Natural Beauty • Culture</p>
    <p>© 2026 Chinaka Enterprises. All Rights Reserved.</p>
</div>
""", unsafe_allow_html=True)
