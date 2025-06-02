import Navbar from "@/components/Navbar";
import Hero from "@/components/Hero";
import { Scroll } from "@/components/scroll";
import Footer from "@/components/Footer";

const Index = () => {
  return (
    <div className="min-h-screen bg-background text-foreground">
      <Navbar />
      <Hero />
      <Scroll />
      <Footer />
    </div>
  );
};

export default Index;
