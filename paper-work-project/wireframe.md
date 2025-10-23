 
## **1. Home / Search Page Wireframe**

```
+--------------------------------------------------------+
| SmartHomesNaija Logo        [Login] [Register] [Menu] |
+--------------------------------------------------------+
| Search Properties:                                     |
| [State Dropdown] [LGA Dropdown] [City/Keyword Input]  |
| [Search Button]                                        |
+--------------------------------------------------------+
| Featured Properties                                     |
| +------------------+ +------------------+             |
| | Property Image   | | Property Image   |             |
| | Title           | | Title           |             |
| | Price           | | Price           |             |
| | Type (Sale/Rent)| | Type (Sale/Rent)|             |
| +------------------+ +------------------+             |
| ...                                                    |
+--------------------------------------------------------+
| Footer: About | Contact | Terms | Privacy             |
+--------------------------------------------------------+
```

---

## **2. Search Results Page Wireframe**

```
+--------------------------------------------------------+
| SmartHomesNaija Logo        [Profile] [Favorites]     |
+--------------------------------------------------------+
| Filters: Price, Type, Bedrooms, Amenities, Distance   |
+--------------------------------------------------------+
| Property List (Grid/List)                              |
| +------------------+  +------------------+           |
| | Property Image   |  | Property Image   |           |
| | Title           |  | Title           |           |
| | Price           |  | Price           |           |
| | Type (Sale/Rent)|  | Type (Sale/Rent)|           |
| | [View Details]  |  | [View Details]  |           |
| +------------------+  +------------------+           |
| Pagination                                             |
+--------------------------------------------------------+
```

---

## **3. Property Detail Page Wireframe**

```
+--------------------------------------------------------+
| [Back to Search]  Property Title                       |
+--------------------------------------------------------+
| Image Gallery / Slider                                 |
| -----------------------------------------------------  |
| | Image 1 | Image 2 | Image 3 | ...                  | 
| -----------------------------------------------------  |
| Price: ₦XXX,XXX  | Type: Sale / Rent | Status: Available |
| Description: Full property description here...        |
| Amenities: [Pool] [Garage] [Garden]                  |
| Owner: Name | Contact Info                             |
| [Add to Favorites]  [Contact Owner]                  |
+--------------------------------------------------------+
| Map: Property location                                  |
+--------------------------------------------------------+
| Similar Properties (Optional)                           |
+--------------------------------------------------------+
```

---

## **4. User Dashboard Wireframe**

```
+--------------------------------------------------------+
| User Dashboard: Name                                    |
+--------------------------------------------------------+
| Favorites:                                             |
| +------------------+ +------------------+             |
| | Property Image   | | Property Image   |             |
| | Title           | | Title           |             |
| | Price           | | Price           |             |
| +------------------+ +------------------+             |
| [Remove from Favorites]                                |
+--------------------------------------------------------+
| Profile Info: Edit Profile, Change Password           |
+--------------------------------------------------------+
```

---

## **5. Subscriber (Property Owner) Dashboard Wireframe**

```
+--------------------------------------------------------+
| Subscriber Dashboard                                   |
+--------------------------------------------------------+
| Add New Listing [Button]                               |
+--------------------------------------------------------+
| My Listings:                                           |
| +------------------+ +------------------+             |
| | Property Image   | | Property Image   |             |
| | Title           | | Title           |             |
| | Price           | | Price           |             |
| | Status: Pending | | Status: Verified|             |
| | [Edit] [Delete] | | [Edit] [Delete] |             |
| +------------------+ +------------------+             |
+--------------------------------------------------------+
```

---

## **6. Admin Panel Wireframe**

```
+--------------------------------------------------------+
| Admin Dashboard                                       |
+--------------------------------------------------------+
| Pending Listings                                      |
| +------------------+ +------------------+             |
| | Property Image   | | Property Image   |             |
| | Title           | | Title           |             |
| | Owner           | | Owner           |             |
| | [Verify] [Reject]| | [Verify] [Reject]|           |
+---------------------+-------------------+-------------+
| User Management: List all users, roles, actions       |
| Analytics: Total Listings | Sold | Available          |
+--------------------------------------------------------+
```

---

✅ These wireframes cover **all MVP pages** visually. You can hand them to a designer, start HTML/CSS, or even build them directly with Flask templates.


## **SmartHomesNaija User Flow / Sitemap**

```
                 ┌─────────────┐
                 │   Home      │
                 │ (Search)    │
                 └─────┬──────┘
                       │
           ┌───────────┴───────────┐
           │                       │
    ┌──────▼───────┐        ┌──────▼───────┐
    │ Search Results│        │ Featured/Hot │
    │   Properties │        │ Properties   │
    └──────┬───────┘        └──────┬───────┘
           │                       │
           │                       │
    ┌──────▼───────┐
    │ Property     │
    │ Detail Page  │
    └──────┬───────┘
           │
   ┌───────▼────────┐
   │ Add to Favorites│
   │ Contact Owner   │
   └───────┬────────┘
           │
   ┌───────▼────────┐
   │ Login/Register │
   └───────┬────────┘
           │
 ┌─────────┴─────────┐
 │   User Dashboard  │
 │ - Favorites       │
 │ - Profile         │
 └─────────┬─────────┘
           │
 ┌─────────▼─────────┐
 │ Subscriber Dashboard │
 │ - Add/Edit Listing   │
 │ - Listing Status     │
 └─────────┬─────────┘
           │
 ┌─────────▼─────────┐
 │ Admin Panel       │
 │ - Verify Listings │
 │ - Manage Users    │
 │ - Analytics       │
 └───────────────────┘
```

---

### **User Roles & Flow Details**

1. **Guest / Regular User**

   * Can view home, search properties, view property details.
   * Must register/login to save favorites, contact owners, or perform actions.

2. **Subscriber (Property Owner)**

   * Can add new property listings.
   * Listings go through admin verification before going live.
   * Can view and manage own listings.

3. **Admin**

   * Verifies or rejects listings.
   * Manages all users and listings.
   * Views analytics: total listings, available, sold/rented.

---

### **Navigation Notes**

* **Header / Navbar**

  * Home, Search, Login/Register, Dashboard (dynamic based on role), Favorites

* **Footer**

  * About, Contact, Terms, Privacy

* **Property Detail Page Actions**

  * Add to Favorites
  * Contact Owner (email/phone)

* **Dashboard Quick Access**

  * Subscribers: “Add Listing”, “My Listings”
  * Admin: “Pending Listings”, “Users”, “Analytics”

---

This sitemap ensures every user knows **where to go, what actions to take, and what role-based content they see**.

---

 