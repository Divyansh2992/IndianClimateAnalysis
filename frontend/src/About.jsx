import React, { useState } from 'react';

export default function About() {
  const [activeTab, setActiveTab] = useState('overview');
  
  // Increase left offset for better centering
  const leftOffset = typeof window !== 'undefined' && window.innerWidth >= 992 ? 180 : 0;
  
  const features = [
          {
        icon: "🌍",
        title: "Comprehensive Coverage",
        description: "All India coverage using verified weather data from ISHRAE, ASHRAE and COLBE."
      },
    {
      icon: "📊",
      title: "Visual Analytics",
      description: "Interactive climate summaries with charts, graphs, and tabular data for better understanding."
    },
    {
      icon: "🏗️",
      title: "Climate Classification",
      description: "Built-in climate zone classification aligned with latest research outcomes."
    },
    {
      icon: "🌡️",
      title: "Psychrometric Analysis",
      description: "Interactive psychrometric analysis with passive design integration for building optimization."
    }
  ];

  const teamMembers = [
    {
      name: "Divyansh Vijay",
      email: "divyanshvijay92@gmail.com",
      role: "B. Tech. (Summer Internship, MNIT Jaipur)",
      institution: "SVNIT Surat",
      image: "/src/assets/divyansh.jpg",
      profileUrl: "https://www.linkedin.com/in/divyansh-vijay-17187b227"
    },
    {
      name: "Raj Gupta",
      email: "guptaa.raj07@gmail.com",
      role: "Research Scholar",
      institution: "MNIT Jaipur",
      image: "/src/assets/RajSir.jpg",
      profileUrl: "https://jouleforgelab.com/"
    },
    {
      name: "Jyotirmay Mathur",
      email: "jmathur.mech@mnit.ac.in",
      role: "Professor",
      institution: "MNIT Jaipur",
      image: "/src/assets/JMSir.jpg",
      profileUrl: "https://mnit.ac.in/dept_mech/profile?fid=Qqs="
    },
    {
      name: "Vishal Garg",
      email: "vishal.garg@plaksha.edu.in",
      role: "Professor",
      institution: "Plaksha University",
      image: "/src/assets/VishalGargSir.jpg",
      profileUrl: "https://plaksha.edu.in/faculty-details/dr-vishal-garg"
    }
  ];

  const sources = [
    {
      name: "ISHRAE",
      url: "https://www.ishrae.in/",
      logo: "/ishrae.png",
      description: "Indian Society of Heating, Refrigerating and Air Conditioning Engineers"
    },
    {
      name: "ASHRAE",
      url: "https://www.ashrae.org/",
      logo: "/ashrae.png",
      description: "American Society of Heating, Refrigerating and Air-Conditioning Engineers"
    },
    {
      name: "COLBE",
      url: "https://colbe.bath.ac.uk/",
      logo: "/colbe.png",
      description: "Climate and Outdoor Laboratory for Building Engineering"
    }
  ];

  return (
    <div className="container py-4" style={{ marginLeft: leftOffset }}>
      <div className="mx-auto" style={{maxWidth: 1000}}>
        {/* Hero Section */}
        <div className="text-center mb-5">
          <h1 className="display-5 fw-bold text-primary mb-3">
            About This Tool
          </h1>
          <div className="lead text-muted mb-4" style={{fontSize: 18, lineHeight: 1.6}}>
            Empowering architects, energy consultants, researchers, and policymakers with 
            <span className="fw-semibold text-primary"> accurate climatic data</span> for sustainable building design.
          </div>
          <div className="bg-light rounded-3 p-3 d-inline-block">
            <span className="badge bg-primary me-2">All India</span>
            <span className="badge bg-success me-2">Verified Data</span>
            <span className="badge bg-info">Interactive Analysis</span>
          </div>
        </div>

        {/* Navigation Tabs */}
        <ul className="nav nav-pills nav-fill mb-4" id="aboutTabs" role="tablist">
          <li className="nav-item" role="presentation">
            <button 
              className={`nav-link ${activeTab === 'overview' ? 'active' : ''}`}
              onClick={() => setActiveTab('overview')}
              type="button"
            >
              <i className="bi bi-info-circle me-2"></i>Overview
            </button>
          </li>
          <li className="nav-item" role="presentation">
            <button 
              className={`nav-link ${activeTab === 'features' ? 'active' : ''}`}
              onClick={() => setActiveTab('features')}
              type="button"
            >
              <i className="bi bi-star me-2"></i>Features
            </button>
          </li>
          <li className="nav-item" role="presentation">
            <button 
              className={`nav-link ${activeTab === 'team' ? 'active' : ''}`}
              onClick={() => setActiveTab('team')}
              type="button"
            >
              <i className="bi bi-people me-2"></i>Team
            </button>
          </li>
          <li className="nav-item" role="presentation">
            <button 
              className={`nav-link ${activeTab === 'sources' ? 'active' : ''}`}
              onClick={() => setActiveTab('sources')}
              type="button"
            >
              <i className="bi bi-link-45deg me-2"></i>Data Sources
            </button>
          </li>
        </ul>

        {/* Tab Content */}
        <div className="tab-content" id="aboutTabContent">
          
          {/* Overview Tab */}
          <div className={`tab-pane fade ${activeTab === 'overview' ? 'show active' : ''}`}>
            <div className="row g-4">
              <div className="col-lg-8">
                <div className="card h-100 border-0 shadow-sm">
                  <div className="card-body p-4">
                    <h3 className="card-title text-primary mb-3">
                      <i className="bi bi-lightbulb me-2"></i>Our Mission
                    </h3>
                    <p className="card-text" style={{fontSize: 16, lineHeight: 1.7}}>
                      This comprehensive climate analysis tool bridges the gap between research and practical application 
                      in sustainable building design. By providing access to verified weather data and advanced analytical 
                      capabilities, we enable professionals to make informed decisions for energy-efficient and 
                      climate-responsive architecture.
                    </p>
                  </div>
                </div>
              </div>
              <div className="col-lg-4">
                <div className="card border-0 shadow-sm h-100">
                  <div className="card-body p-4">
                    <h4 className="card-title text-primary mb-3">
                      <i className="bi bi-graph-up me-2"></i>Key Statistics
                    </h4>
                    <div className="d-flex flex-column gap-3">
                      <div className="text-center p-3 bg-primary bg-opacity-10 rounded">
                        <div className="h3 text-primary mb-1">All India</div>
                        <div className="text-muted small">Coverage</div>
                      </div>
                      <div className="text-center p-3 bg-success bg-opacity-10 rounded">
                        <div className="h3 text-success mb-1">3</div>
                        <div className="text-muted small">Data Sources</div>
                      </div>
                      <div className="text-center p-3 bg-info bg-opacity-10 rounded">
                        <div className="h3 text-info mb-1">4</div>
                        <div className="text-muted small">Core Features</div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Features Tab */}
          <div className={`tab-pane fade ${activeTab === 'features' ? 'show active' : ''}`}>
            <div className="row g-4">
              {features.map((feature, index) => (
                <div key={index} className="col-md-6 col-lg-3">
                  <div className="card h-100 border-0 shadow-sm hover-lift">
                    <div className="card-body p-4 text-center">
                      <div className="display-6 mb-3">{feature.icon}</div>
                      <h5 className="card-title text-primary mb-3">{feature.title}</h5>
                      <p className="card-text text-muted" style={{fontSize: 14, lineHeight: 1.6}}>
                        {feature.description}
                      </p>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Team Tab */}
          <div className={`tab-pane fade ${activeTab === 'team' ? 'show active' : ''}`}>
            <div className="row g-4">
              {teamMembers.map((member, index) => (
                <div key={index} className="col-md-6 col-lg-3">
                  <div className="card h-100 border-0 shadow-sm hover-lift text-center">
                    <div className="card-body p-4">
                      <div className="mb-3 d-flex justify-content-center">
                        <img 
                          src={member.image} 
                          alt={`${member.name} profile`}
                          className="rounded-circle"
                          style={{
                            width: '80px',
                            height: '80px',
                            objectFit: 'cover',
                            border: '3px solid #f8f9fa',
                            boxShadow: '0 2px 8px rgba(0,0,0,0.1)'
                          }}
                        />
                      </div>
                      <h5 className="card-title text-primary mb-2">
                        {member.profileUrl ? (
                          <a 
                            href={member.profileUrl} 
                            target="_blank" 
                            rel="noopener noreferrer"
                            className="text-decoration-none"
                            title="View Profile"
                          >
                            {member.name}
                            <i className="bi bi-box-arrow-up-right ms-1" style={{fontSize: '0.8em'}}></i>
                          </a>
                        ) : (
                          member.name
                        )}
                      </h5>
                      <p className="text-muted small mb-2">
                        <i className="bi bi-envelope me-1"></i>
                        <a href={`mailto:${member.email}`} className="text-decoration-none">
                          {member.email}
                        </a>
                      </p>
                      <p className="text-success fw-semibold mb-1">{member.role}</p>
                      <p className="text-muted small">{member.institution}</p>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Sources Tab */}
          <div className={`tab-pane fade ${activeTab === 'sources' ? 'show active' : ''}`}>
            {/* Research Collaboration Section */}
            <div className="mb-4">
              <h5 className="text-success mb-2">
                <i className="bi bi-people me-2"></i>Research Collaboration
              </h5>
              <p className="text-muted mb-2">
                Our climate zone classification is aligned with the latest research outcomes.
              </p>
              <div className="bg-light rounded p-3 border-start border-4 border-primary">
                <small className="text-muted">
                  <strong>R. Gupta, J. Mathur, and V. Garg</strong>, "A criteria-based climate classification approach 
                  considering clustering and building thermal performance: Case of India", 
                  <em>Build. Environ.</em>, vol. 270, no. December 2024, p. 112512, 2025.
                </small>
                <br/>
                <a 
                  href="https://doi.org/10.1016/j.buildenv.2024.112512" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="btn btn-sm btn-outline-primary mt-2"
                >
                  <i className="bi bi-box-arrow-up-right me-1"></i>View Publication
                </a>
              </div>
            </div>
            {/* Data Sources List */}
            <div className="row g-4">
              {sources.map((source, index) => (
                <div key={index} className="col-md-4">
                  <div className="card h-100 border-0 shadow-sm hover-lift">
                    <div className="card-body p-4 text-center">
                      <a 
                        href={source.url} 
                        target="_blank" 
                        rel="noopener noreferrer"
                        className="text-decoration-none"
                      >
                        <img 
                          src={source.logo} 
                          alt={`${source.name} Logo`} 
                          className="img-fluid rounded bg-light p-3 border mb-3" 
                          style={{height: 80, objectFit: 'contain', transition: 'transform 0.2s'}}
                          onMouseOver={(e) => e.target.style.transform = 'scale(1.05)'}
                          onMouseOut={(e) => e.target.style.transform = 'scale(1)'}
                        />
                      </a>
                      <h5 className="card-title text-primary mb-2">{source.name}</h5>
                      <p className="card-text text-muted small" style={{lineHeight: 1.5}}>
                        {source.description}
                      </p>
                      <a 
                        href={source.url} 
                        target="_blank" 
                        rel="noopener noreferrer"
                        className="btn btn-outline-primary btn-sm"
                      >
                        <i className="bi bi-box-arrow-up-right me-1"></i>Visit Website
                      </a>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      <style>{`
        .hover-lift {
          transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        }
        .hover-lift:hover {
          transform: translateY(-5px);
          box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15) !important;
        }
        .nav-pills .nav-link {
          border-radius: 50px;
          padding: 0.75rem 1.5rem;
          font-weight: 500;
          transition: all 0.2s ease-in-out;
        }
        .nav-pills .nav-link:hover {
          transform: translateY(-1px);
        }
        .card {
          transition: all 0.2s ease-in-out;
        }
        .badge {
          font-size: 0.8rem;
          padding: 0.5rem 0.75rem;
        }
      `}</style>
    </div>
  );
} 
