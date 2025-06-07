import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import {
  Target,
  Eye,
  Users,
  TrendingUp,
  Shield,
  Star,
  ArrowRight,
} from "lucide-react";

const AboutUs = () => {
  const values = [
    {
      id: 1,
      title: "Expert-Driven Insights",
      description:
        "Connect with SEBI-registered research analysts and advisors for trusted expertise",
      icon: Shield,
      color: "blue",
    },
    {
      id: 2,
      title: "Transparent Guidance",
      description:
        "Every investment choice backed by credible and transparent research",
      icon: Star,
      color: "green",
    },
    {
      id: 3,
      title: "Retail Investor Focus",
      description:
        "Empowering individual investors with professional-grade market insights",
      icon: Users,
      color: "purple",
    },
  ];

  return (
    <div className="min-h-screen bg-background text-foreground">
      <Navbar />

      {/* Hero Section */}
      <section className="pt-20 pb-16 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto text-center">
          <div className="inline-flex items-center space-x-2 bg-secondary/50 px-4 py-2 rounded-full mb-6">
            <Target className="h-4 w-4 text-blue-400" />
            <span className="text-sm text-muted-foreground">
              Trusted by Investors
            </span>
          </div>

          <h1 className="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-white via-gray-200 to-gray-400 bg-clip-text text-transparent">
            About Us
          </h1>

          <p className="text-xl text-muted-foreground mb-8 max-w-4xl mx-auto leading-relaxed">
            At Tradepeeps, we believe that successful investing begins with
            credible, transparent, and expert-driven insights. Navigating the
            stock market can be complex, but with the right guidance, every
            investor can make informed decisions.
          </p>

          <div className="flex flex-wrap justify-center gap-4 mb-12">
            <div className="flex items-center space-x-2 bg-card border border-border rounded-lg px-4 py-2">
              <Shield className="h-5 w-5 text-blue-400" />
              <span className="text-sm">SEBI-Registered Experts</span>
            </div>
            <div className="flex items-center space-x-2 bg-card border border-border rounded-lg px-4 py-2">
              <TrendingUp className="h-5 w-5 text-green-400" />
              <span className="text-sm">Trusted Insights</span>
            </div>
            <div className="flex items-center space-x-2 bg-card border border-border rounded-lg px-4 py-2">
              <Users className="h-5 w-5 text-purple-400" />
              <span className="text-sm">Retail Investor Focused</span>
            </div>
          </div>
        </div>
      </section>

      {/* Mission & Vision Section */}
      <section className="py-16 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-16">
            <Card className="relative overflow-hidden transition-all duration-300 hover:scale-105 hover:shadow-xl border-blue-400 shadow-lg">
              <div className="absolute top-4 right-4 z-10">
                <Badge className="bg-blue-400 text-black font-semibold">
                  <Target className="h-3 w-3 mr-1" />
                  Mission
                </Badge>
              </div>

              <CardHeader className="pb-4">
                <CardTitle className="text-2xl font-bold text-blue-400">
                  Our Mission
                </CardTitle>
                <CardDescription className="text-muted-foreground text-lg">
                  Bridging the gap between investors and experts
                </CardDescription>
              </CardHeader>

              <CardContent className="space-y-6">
                <p className="text-foreground leading-relaxed">
                  To bridge the gap between retail investors and verified
                  financial experts, providing access to high-quality investment
                  research and strategies.
                </p>

                <Button className="w-full bg-blue-400 hover:bg-blue-500 text-black transition-all duration-300">
                  Learn More About Our Mission
                  <ArrowRight className="h-4 w-4 ml-2" />
                </Button>
              </CardContent>
            </Card>

            <Card className="relative overflow-hidden transition-all duration-300 hover:scale-105 hover:shadow-xl border-green-400 shadow-lg">
              <div className="absolute top-4 right-4 z-10">
                <Badge className="bg-green-400 text-black font-semibold">
                  <Eye className="h-3 w-3 mr-1" />
                  Vision
                </Badge>
              </div>

              <CardHeader className="pb-4">
                <CardTitle className="text-2xl font-bold text-green-400">
                  Our Vision
                </CardTitle>
                <CardDescription className="text-muted-foreground text-lg">
                  Leading India's investment platform
                </CardDescription>
              </CardHeader>

              <CardContent className="space-y-6">
                <p className="text-foreground leading-relaxed">
                  To establish Tradepeeps as India's most trusted platform for
                  market insights, enabling investors to navigate the stock
                  market with confidence and expert guidance.
                </p>

                <Button className="w-full bg-green-400 hover:bg-green-500 text-black transition-all duration-300">
                  Explore Our Vision
                  <ArrowRight className="h-4 w-4 ml-2" />
                </Button>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Core Values Section */}
      <section className="py-16 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold mb-6">
              What Makes Us
              <span className="bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
                {" "}
                Different
              </span>
            </h2>
            <p className="text-xl text-muted-foreground max-w-3xl mx-auto">
              Our platform empowers retail investors by connecting them with
              SEBI-registered research analysts and advisors, ensuring that
              every investment choice is backed by trusted expertise.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {values.map((value) => {
              const IconComponent = value.icon;
              return (
                <Card
                  key={value.id}
                  className="relative overflow-hidden transition-all duration-300 hover:scale-105 hover:shadow-xl"
                >
                  <CardHeader className="pb-4 text-center">
                    <div
                      className={`mx-auto mb-4 p-3 rounded-full w-fit ${
                        value.color === "blue"
                          ? "bg-blue-400/10"
                          : value.color === "green"
                          ? "bg-green-400/10"
                          : "bg-purple-400/10"
                      }`}
                    >
                      <IconComponent
                        className={`h-8 w-8 ${
                          value.color === "blue"
                            ? "text-blue-400"
                            : value.color === "green"
                            ? "text-green-400"
                            : "text-purple-400"
                        }`}
                      />
                    </div>
                    <CardTitle className="text-xl font-bold">
                      {value.title}
                    </CardTitle>
                  </CardHeader>

                  <CardContent>
                    <p className="text-muted-foreground text-center leading-relaxed">
                      {value.description}
                    </p>
                  </CardContent>
                </Card>
              );
            })}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-6">
            Ready to Start Your
            <span className="bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
              {" "}
              Investment Journey?
            </span>
          </h2>
          <p className="text-xl text-muted-foreground mb-8">
            Join thousands of investors who trust Tradepeeps for expert market
            insights and guidance.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button
              size="lg"
              className="bg-white text-black hover:bg-gray-200 transition-colors"
            >
              Get Started Today
            </Button>
            <Button
              size="lg"
              variant="outline"
              className="border-border hover:bg-secondary"
            >
              Contact Our Experts
            </Button>
          </div>
        </div>
      </section>

      <Footer />
    </div>
  );
};

export default AboutUs;
