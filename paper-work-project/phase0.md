 

## **Phase 0 — Planning for SmartHomesNaija**

### **Step 1: Finalize Feature List & Prioritize (MVP vs Later)**

**MVP (Minimum Viable Product)** — features required for first usable version:

* User registration/login (with email verification)
* Search properties by state, LGA, city
* Property detail page (images, basic info, price, owner/agent)
* Favorite/save properties
* Property owner (subscriber) can create listing
* Admin can verify listings
* Property status: available / sold / rented
* Basic analytics: total listings, available vs sold

**Phase 2+ Features (can add later)**

* Payment gateway integration (Stripe, Paystack, Flutterwave)
* Map directions & distance-based search
* Video media for property listings
* Advanced filters (bedrooms, price range, amenities)
* Chatbot for customer support
* Dashboard analytics graphs & revenue tracking
* SMS/email notifications

---

### **Step 2: Create Wireframes (Sketch Out Main Pages)**

**Main pages for the MVP:**

1. **Home / Search page**

   * Search bar: state, LGA, city
   * Featured properties section
2. **Search results page**

   * List of properties with thumbnail, price, type (sale/rent)
   * Pagination
3. **Property detail page**

   * Full description, images, owner info, property stats
   * Favorite button
4. **User dashboard**

   * Favorites
   * User details
5. **Subscriber dashboard (property owner)**

   * Add/edit listings
   * View listing status (verified/pending/rejected)
6. **Admin panel**

   * Verify listings
   * View users and properties
   * Basic analytics (counts of listings, sold/available)

---

### **Step 3: Design Database Schema**

**Core tables:**

1. **users**

   * id (PK), name, email, phone, role [user/subscriber/admin], password_hash, created_at

2. **properties**

   * id (PK), owner_id (FK → users), title, description, price, type [sale/rent], rent_period, state, lga, city, address, latitude, longitude, verified (bool), status [available/sold/let], created_at, updated_at

3. **property_media**

   * id (PK), property_id (FK → properties), file_url, media_type [image/video], caption

4. **favorites**

   * id (PK), user_id (FK → users), property_id (FK → properties), created_at

5. **transactions** *(optional for later)*

   * id (PK), user_id (FK → users), property_id (FK → properties), amount, currency, payment_status, payment_provider, type [deposit/purchase/rent], created_at

6. **analytics_events** *(optional for later)*

   * id, property_id, user_id, event_type [view/favorite/inquiry], timestamp

7. **chats/messages** *(optional for later)*

   * id, user_id, message, timestamp, sender [user/bot/admin]

---

### **Step 4: Design API Endpoints / Routes (MVP)**

**User-related routes:**

* POST `/register` → create account
* POST `/login` → authenticate
* GET `/profile` → get user info
* PUT `/profile` → update info

**Property-related routes:**

* GET `/properties` → search/list properties
* GET `/properties/<id>` → property detail
* POST `/properties` → create new property (subscriber)
* PUT `/properties/<id>` → edit property (owner/admin)
* DELETE `/properties/<id>` → remove property (owner/admin)

**Favorites routes:**

* POST `/favorites/<property_id>` → add to favorites
* GET `/favorites` → list favorites
* DELETE `/favorites/<property_id>` → remove from favorites

**Admin routes:**

* GET `/admin/properties` → list pending listings
* POST `/admin/properties/<id>/verify` → approve listing
* POST `/admin/properties/<id>/reject` → reject listing
* GET `/admin/users` → list all users

---

### **Step 5: Define Tools & Tech Stack**

* **Backend:** Python + Flask
* **Database:** PostgreSQL (+PostGIS later for map searches)
* **ORM:** SQLAlchemy / Flask-SQLAlchemy
* **Frontend:** Flask templates + Bootstrap or Tailwind
* **Maps:** Leaflet / Google Maps API
* **Payments:** Stripe / Paystack / Flutterwave (later)
* **Hosting:** DigitalOcean / AWS / Heroku

---

✅ **Outcome of Phase 0:**

* Clear MVP feature list
* Wireframes/sketches of main pages
* Database schema design
* API endpoints plan
* Defined tech stack

 