from crewai import Task

def requirement_task(agent, user_input):
    return Task(

        description=f"""
        You are a world-class UI/UX designer and product architect.

        A user wants to generate a beautiful, production-ready website.

        USER INPUT:
        {user_input}

        Your job is to extract EXTREMELY DETAILED design and technical requirements.

        You must specify:

        1. WEBSITE TYPE & PERSONALITY
           - Type (SaaS, portfolio, restaurant, e-commerce, startup, etc.)
           - Brand personality (luxury, playful, minimal, bold, futuristic, etc.)
           - Target audience and emotional tone

        2. COLOR PALETTE (be specific with hex codes or descriptive names)
           - Primary background color (dark or light gradient?)
           - Accent/highlight color (vibrant purple? electric blue? warm orange?)
           - Text colors (pure white, off-white, muted grays)
           - Card/panel background colors
           - Gradient direction and values

        3. TYPOGRAPHY
           - Heading font style (bold, heavy weight, tight tracking)
           - Body font (clean, readable, modern)
           - Font sizes (hero title large? 4xl-7xl)

        4. PAGES & SECTIONS (list every section needed)
           - Navbar with logo, links, and CTA button
           - Hero section with big headline, subtext, CTA buttons, and background design (gradient blob, grid pattern, particles, etc.)
           - Features/Services section with icon cards
           - Testimonials or social proof section
           - Pricing or Gallery section (if applicable)
           - Contact or CTA section
           - Footer with links and copyright

        5. ANIMATIONS (be very detailed)
           - Hero content: fade-in from bottom on load
           - Section reveals: elements animate in as user scrolls (viewport-based)
           - Cards: hover lift effect with shadow glow
           - Buttons: hover scale and glow on interaction
           - Navbar: transparent → blur backdrop on scroll
           - Icons: rotate or pulse on hover
           - Images or mockups: float animation

        6. LAYOUT & SPACING
           - Max-width containers (max-w-7xl centered)
           - Section padding (py-20 to py-32)
           - Grid and flex layouts for cards

        7. SPECIAL DESIGN ELEMENTS
           - Glassmorphism cards (backdrop-blur, transparent borders)
           - Gradient text on headlines
           - Glowing CTA buttons with shimmer effect
           - Subtle grid or dot background patterns
           - Animated gradient orbs as background accents

        Be extremely detailed. Do NOT summarize. The React developer needs this to build a STUNNING website.
        """,
        expected_output="""
        Ultra-detailed design specification including:
        * Website type and brand personality
        * Exact color palette with accent and gradient details
        * Typography recommendations
        * Full list of sections with content requirements
        * Animation plan per section (Framer Motion specific)
        * Layout and spacing details
        * Special design elements (glassmorphism, glows, patterns)
        """,
        agent=agent
    )

def react_code_task(agent, requirements):

    return Task(
        description=f"""
        You are a WORLD-CLASS senior React developer and UI engineer who creates breathtaking, production-grade websites.

        REQUIREMENTS FROM DESIGNER:
        {requirements}

        ════════════════════════════════════════════
        YOU MUST BUILD A VISUALLY STUNNING WEBSITE.
        This must look like it came from a top-tier design agency.
        SIMPLE OR PLAIN CODE IS NOT ACCEPTABLE.
        ════════════════════════════════════════════

        ── DESIGN MANDATORIES ──────────────────────

        1. COLOR & THEME
           - Use a rich, dark background: `bg-gray-950` or `bg-neutral-950` or custom gradient like `#0a0a0f`
           - Use vibrant accent colors: indigo, violet, purple, cyan, or amber (pick one brand color and use it consistently)
           - Gradient text on ALL main headings: use inline style `background: 'linear-gradient(135deg, #fff, #a78bfa)'` with `-webkit-background-clip: text` and `-webkit-text-fill-color: transparent`
           - Glassmorphism cards: `bg-white/5 backdrop-blur-sm border border-white/10 rounded-2xl`
           - Glowing buttons: add `box-shadow` glow matching the accent color on hover

        2. TYPOGRAPHY
           - Import Inter font: add `<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet" />` in index.html
           - Set `font-family: 'Inter', sans-serif` on body in index.css
           - Hero headline: text-5xl to text-7xl, font-black, tight tracking (-0.03em letter-spacing)
           - Section headings: text-3xl to text-5xl, font-bold
           - Use gradient text on every major heading using the pattern above

        3. BACKGROUND DESIGN
           - The hero section MUST have a stunning background. Use ONE of these approaches:
             Option A: Gradient + SVG blur orbs (colorful blobs in background)
             ```jsx
             <div style={{position:'absolute',inset:0,overflow:'hidden',zIndex:0}}>
               <div style={{position:'absolute',top:'-20%',left:'30%',width:'600px',height:'600px',
                 background:'radial-gradient(circle, rgba(139,92,246,0.3) 0%, transparent 70%)',
                 filter:'blur(80px)',borderRadius:'50%'}} />
               <div style={{position:'absolute',bottom:'-10%',right:'20%',width:'500px',height:'500px',
                 background:'radial-gradient(circle, rgba(59,130,246,0.2) 0%, transparent 70%)',
                 filter:'blur(60px)',borderRadius:'50%'}} />
             </div>
             ```
             Option B: Subtle grid pattern overlay using CSS background-image

        4. FRAMER MOTION ANIMATIONS (ALL MANDATORY)
           Import at top of EVERY component file:
           ```jsx
           import {{ motion, AnimatePresence, useAnimation }} from 'framer-motion';
           import {{ useEffect, useRef }} from 'react';
           ```

           USE THESE EXACT PATTERNS:

           A. Hero fade-in on load:
           ```jsx
           <motion.div
             initial={{opacity:0, y:40}}
             animate={{opacity:1, y:0}}
             transition={{duration:0.8, ease:[0.16,1,0.3,1]}}
           >
           ```

           B. Stagger children animations:
           ```jsx
           const containerVariants = {{
             hidden: {{}},
             visible: {{ transition: {{ staggerChildren: 0.15 }} }}
           }};
           const itemVariants = {{
             hidden: {{ opacity: 0, y: 30 }},
             visible: {{ opacity: 1, y: 0, transition: {{ duration: 0.6, ease: [0.16,1,0.3,1] }} }}
           }};
           <motion.div variants={{containerVariants}} initial="hidden" whileInView="visible" viewport={{{{once:true, margin:'-50px'}}}}>
             <motion.div variants={{itemVariants}}>...</motion.div>
             <motion.div variants={{itemVariants}}>...</motion.div>
           </motion.div>
           ```

           C. Card hover with glow:
           ```jsx
           <motion.div
             whileHover={{y:-8, scale:1.02, boxShadow:'0 20px 60px rgba(139,92,246,0.25)'}}
             transition={{type:'spring', stiffness:300, damping:20}}
             style={{background:'rgba(255,255,255,0.03)', backdropFilter:'blur(12px)',
               border:'1px solid rgba(255,255,255,0.08)', borderRadius:'16px', padding:'24px'}}
           >
           ```

           D. Button hover glow:
           ```jsx
           <motion.button
             whileHover={{scale:1.05, boxShadow:'0 0 30px rgba(139,92,246,0.5)'}}
             whileTap={{scale:0.98}}
             style={{background:'linear-gradient(135deg,#7c3aed,#4f46e5)',...}}
           >
           ```

           E. Floating animation (for images/icons):
           ```jsx
           <motion.div
             animate={{y:[0,-15,0]}}
             transition={{duration:4, repeat:Infinity, ease:'easeInOut'}}
           >
           ```

        5. NAVBAR
           - Fixed position: `style={{position:'fixed', top:0, left:0, right:0, zIndex:50}}`
           - Glassmorphism: `style={{backdropFilter:'blur(20px)', background:'rgba(10,10,20,0.8)', borderBottom:'1px solid rgba(255,255,255,0.06)'}}`
           - Logo with gradient icon
           - Nav links with hover underline animation
           - Animated CTA button

        6. HERO SECTION
           - Full viewport height: `style={{minHeight:'100vh', display:'flex', alignItems:'center'}}`
           - Animated badge/label at top: small pill with gradient border
           - Giant headline with gradient text (3-5 lines max)
           - Descriptive subtext in muted gray
           - TWO CTA buttons: one primary gradient, one ghost/outline
           - Below fold: animated stats row OR trust badges (e.g., "5000+ customers", "★ 4.9/5")
           - BACKGROUND: gradient orbs (use Option A from point 3)

        7. FEATURES/CARDS SECTION
           - Section label: small uppercase text in accent color
           - Section heading with gradient text
           - Grid of 3-6 cards with:
             * Icon (use emoji OR create SVG icon inline)
             * Card title
             * Description
             * Glassmorphism styling
             * Hover glow animation

        8. TESTIMONIALS SECTION
           - At least 3 testimonial cards
           - Avatar initial circle with gradient background
           - Star rating display (★★★★★)
           - Quote in italic
           - Name and role

        9. CTA/FOOTER SECTION
           - Big centered headline with gradient text
           - Primary CTA button
           - Animated background orbs
           - Footer with logo, links in columns, copyright line

        ── TECHNICAL RULES ─────────────────────────

        * Use ONLY inline styles OR Tailwind classes. No CSS modules.
        * Every motion.div must have valid motion import.
        * DO NOT use react-router-dom unless generating a multi-page app.
        * All icons: use emoji OR simple SVG inline. Do NOT import from icon libraries.
        * src/index.css MUST contain:
          ```
          @tailwind base;
          @tailwind components;
          @tailwind utilities;

          * {{ box-sizing: border-box; margin: 0; padding: 0; }}
          body {{ font-family: 'Inter', system-ui, sans-serif; background: #09090f; color: #f1f5f9; }}
          ::-webkit-scrollbar {{ width: 6px; }}
          ::-webkit-scrollbar-track {{ background: #0a0a0f; }}
          ::-webkit-scrollbar-thumb {{ background: #7c3aed; border-radius: 3px; }}
          ```

        ── OUTPUT FORMAT ────────────────────────────

        Output files with FILE markers ONLY. NO explanations, NO text outside file blocks.

        FILE: package.json
        ```json
        code here
        ```

        FILE: vite.config.js
        ```javascript
        code here
        ```

        FILE: tailwind.config.js
        ```javascript
        code here
        ```

        FILE: postcss.config.js
        ```javascript
        code here
        ```

        FILE: index.html
        ```html
        code here
        ```

        FILE: src/main.jsx
        ```javascript
        code here
        ```

        FILE: src/App.jsx
        ```javascript
        code here
        ```

        FILE: src/index.css
        ```css
        code here
        ```

        FILE: src/components/Navbar.jsx
        ```javascript
        code here
        ```

        FILE: src/components/Hero.jsx
        ```javascript
        code here
        ```

        FILE: src/components/Features.jsx
        ```javascript
        code here
        ```

        FILE: src/components/Testimonials.jsx
        ```javascript
        code here
        ```

        FILE: src/components/Footer.jsx
        ```javascript
        code here
        ```

        CRITICAL RULES:
        * NEVER IMPORT A FILE YOU HAVE NOT GENERATED.
        * DO NOT import from './Link', './Icon', './Button' unless you have a FILE: for it.
        * Every component that uses motion MUST import it: `import {{ motion }} from 'framer-motion'`
        * Generate ALL files referenced in imports.
        """,
        expected_output="""
        A complete, stunning React project with FILE markers containing:
        - Glassmorphism UI cards
        - Gradient text headings
        - Framer Motion animations on every section
        - Rich dark background with gradient orbs
        - Professional Navbar, Hero, Features, Testimonials, Footer
        - All files generated and importable
        """,
        agent=agent
    )
