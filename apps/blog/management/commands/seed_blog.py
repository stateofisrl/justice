from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.blog.models import Category, BlogPost


class Command(BaseCommand):
    help = 'Seed the database with blog content'

    def handle(self, *args, **options):
        # Create categories
        fraud_awareness, _ = Category.objects.get_or_create(
            name='Fraud Awareness',
            defaults={'slug': 'fraud-awareness'}
        )
        recovery_stories, _ = Category.objects.get_or_create(
            name='Recovery Stories',
            defaults={'slug': 'recovery-stories'}
        )
        cyber_tips, _ = Category.objects.get_or_create(
            name='Cyber Tips',
            defaults={'slug': 'cyber-tips'}
        )

        # Get or create admin user
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@cyberintelligence.com',
                'first_name': 'Admin',
                'last_name': 'User',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()

        # Post 1: How Cyber Intelligence Tracks Scammers
        post1, created = BlogPost.objects.get_or_create(
            slug='how-cyber-intelligence-tracks-scammers',
            defaults={
                'title': 'How Cyber Intelligence Tracks Scammers',
                'category': fraud_awareness,
                'author': admin_user,
                'excerpt': 'Discover how advanced digital forensics and intelligence techniques help identify and trace fraudsters across the globe.',
                'body': '''
<h2>Understanding Digital Footprints</h2>
<p>Every scammer leaves a digital trace. From IP addresses and email headers to cryptocurrency transactions and social media profiles, modern cyber intelligence combines multiple data sources to build a complete picture of fraudulent operations.</p>

<h3>Key Tracking Methods</h3>
<ul>
<li><strong>IP Address Analysis:</strong> Track the geographic location and internet service provider behind criminal activity</li>
<li><strong>Transaction Monitoring:</strong> Follow money trails through blockchain networks and traditional financial systems</li>
<li><strong>Social Engineering Detection:</strong> Identify patterns in how scammers impersonate legitimate organizations</li>
<li><strong>Device Fingerprinting:</strong> Recognize when the same criminal uses multiple accounts</li>
</ul>

<h2>Blockchain Analysis</h2>
<p>Cryptocurrency scams often rely on the false assumption that blockchain transactions are untraceable. Advanced analysis tools can:</p>
<ul>
<li>Track crypto movements across exchanges</li>
<li>Identify wallet clustering patterns</li>
<li>Monitor money laundering attempts</li>
<li>Recover funds before they're converted to fiat currency</li>
</ul>

<h2>Cooperation with Financial Institutions</h2>
<p>Banks and payment processors maintain detailed records of suspicious transactions. When combined with law enforcement cooperation, these records help us identify and stop scammers before they can move their victims' money offshore.</p>

<h2>Why Time Matters</h2>
<p>The first 24-48 hours are critical. The sooner we're notified of a scam, the better our chances of:</p>
<ul>
<li>Freezing accounts before funds are transferred</li>
<li>Recovering cryptocurrency in transit</li>
<li>Identifying other victims of the same operation</li>
<li>Building a case for prosecution</li>
</ul>

<p>If you've been victimized by a scam, contact us immediately. Every hour counts in the recovery process.</p>
                ''',
                'tags': 'scam tracing, cyber intelligence, digital forensics',
                'published': True
            }
        )

        # Post 2: Top 5 Online Scam Red Flags
        post2, created = BlogPost.objects.get_or_create(
            slug='top-5-online-scam-red-flags',
            defaults={
                'title': 'Top 5 Online Scam Red Flags',
                'category': cyber_tips,
                'author': admin_user,
                'excerpt': 'Learn to identify common warning signs that can help you avoid becoming a victim of online fraud.',
                'body': '''
<h2>Red Flag #1: Pressure to Act Quickly</h2>
<p>Legitimate companies don't rush you into decisions. If someone is pushing you to make an immediate payment or transfer funds within hours, it's almost certainly a scam.</p>
<ul>
<li>"Act now or your account will be closed"</li>
<li>"Limited time offer - invest today"</li>
<li>"You must wire the money by 5 PM today"</li>
</ul>

<h2>Red Flag #2: Requests for Personal Information</h2>
<p>Real banks and legitimate companies will never ask you to:</p>
<ul>
<li>Provide your full password or PIN</li>
<li>Share your Social Security Number via email</li>
<li>Confirm credit card details in unsolicited messages</li>
<li>Click links to "verify" your information</li>
</ul>

<h2>Red Flag #3: Too Good to Be True</h2>
<p>If the opportunity sounds too good, it definitely is:</p>
<ul>
<li>Guaranteed investment returns of 10% or more per month</li>
<li>Easy money with minimal effort</li>
<li>Unrealistic job offers with high pay</li>
<li>Free money with no strings attached</li>
</ul>

<h2>Red Flag #4: Inconsistencies and Poor Communication</h2>
<p>Professional organizations maintain consistent branding and communication standards:</p>
<ul>
<li>Grammar and spelling errors in official emails</li>
<li>Generic greetings like "Dear Customer" instead of your name</li>
<li>Mismatched email addresses or phone numbers</li>
<li>Different logos or branding from official sources</li>
</ul>

<h2>Red Flag #5: Requests for Unusual Payment Methods</h2>
<p>Legitimate businesses use secure, traceable payment methods:</p>
<ul>
<li>Requests for cryptocurrency, gift cards, or wire transfers</li>
<li>Asking you to pay first, then receive goods/services</li>
<li>Using money transfer apps instead of official payment systems</li>
<li>Requests to move money to a different account</li>
</ul>

<h2>What to Do if You Spot These Red Flags</h2>
<ol>
<li>Stop all communication with the suspicious party</li>
<li>Do not provide any additional information</li>
<li>Contact the official company directly using verified contact information</li>
<li>Report the incident to the FBI's Internet Crime Complaint Center (IC3)</li>
<li>If you've already lost money, contact Cyber Intelligence immediately</li>
</ol>

<p>Trust your instincts. If something feels off, it probably is.</p>
                ''',
                'tags': 'scam prevention, red flags, fraud detection',
                'published': True
            }
        )

        # Post 3: Real Stories - Victims Who Fought Back
        post3, created = BlogPost.objects.get_or_create(
            slug='real-stories-victims-who-fought-back',
            defaults={
                'title': 'Real Stories: Victims Who Fought Back',
                'category': recovery_stories,
                'author': admin_user,
                'excerpt': 'Inspiring case studies of victims who successfully recovered from online scams with our help.',
                'body': '''
<h2>Case Study #1: The Investment Scam Recovery</h2>
<p><strong>Victim:</strong> Sarah M., Age 58</p>
<p><strong>The Scam:</strong> Sarah was contacted through Facebook by someone claiming to be a cryptocurrency investment advisor. After several weeks of building trust, she was convinced to invest $45,000 in a "guaranteed" blockchain fund.</p>
<p><strong>The Recovery:</strong> Within 48 hours of contacting Cyber Intelligence, we:</p>
<ul>
<li>Traced the cryptocurrency address to an exchange in Eastern Europe</li>
<li>Worked with the exchange to identify the recipient account</li>
<li>Coordinated with law enforcement to freeze the account</li>
<li>Successfully recovered $42,300 (94% of the original amount)</li>
</ul>
<p><strong>Timeline:</strong> 21 days from report to recovery</p>

<h2>Case Study #2: The Romance Scam Turnabout</h2>
<p><strong>Victim:</strong> James T., Age 72</p>
<p><strong>The Scam:</strong> James met "Catherine" on a dating website. Over 6 months, they built an emotional connection. When "Catherine" claimed to need money for medical emergencies and business ventures, James transferred $78,000.</p>
<p><strong>The Recovery:</strong> Our investigators:</p>
<ul>
<li>Identified the scam network operating from multiple locations</li>
<li>Traced the victims' money to a money laundering operation</li>
<li>Recovered $54,000 through international bank cooperation</li>
<li>Helped prosecute 3 members of the criminal organization</li>
</ul>
<p><strong>Timeline:</strong> 45 days from report to partial recovery and prosecution</p>

<h2>Case Study #3: The Tech Support Scam Victory</h2>
<p><strong>Victim:</strong> Margaret L., Age 65</p>
<p><strong>The Scam:</strong> Margaret received a pop-up warning that her computer was infected. She called the number provided and gave remote access to a "technician" who convinced her to wire $3,500 for "software fixes."</p>
<p><strong>The Recovery:</strong> Because Margaret acted immediately:</p>
<ul>
<li>We contacted her bank within 2 hours</li>
<li>The wire transfer was intercepted before being deposited</li>
<li>All funds were returned to her account</li>
<li>The bank closed the receiving account and reported the operation</li>
</ul>
<p><strong>Timeline:</strong> 4 hours from report to full recovery</p>

<h2>Key Lessons from Successful Cases</h2>
<ol>
<li><strong>Act Quickly:</strong> The faster you report a scam, the better our chances of recovery</li>
<li><strong>Preserve Evidence:</strong> Save all emails, messages, and transaction records</li>
<li><strong>Don't Give Up:</strong> Even in complex cases, recovery is possible with persistence</li>
<li><strong>Get Support:</strong> Victims often experience shame; our counselors help with emotional recovery too</li>
<li><strong>Help Others:</strong> Information you provide helps us stop these criminals from victimizing others</li>
</ol>

<h2>You Can Fight Back</h2>
<p>If you've been victimized by a scam, don't suffer in silence. Contact Cyber Intelligence today. Like Sarah, James, and Margaret, you may be able to recover your funds and help justice prevail.</p>

<p><a href="/support/ticket/new/">Submit your case now →</a></p>
                ''',
                'tags': 'recovery stories, success cases, scam victims',
                'published': True
            }
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded blog content'))
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created admin user: {admin_user.username}'))
