import { Button } from "../components/ui/button";
import { Code2 } from "lucide-react";

const Navbar = () => {
  return (
    <nav className="border-b border-border/40 bg-background/80 backdrop-blur-sm sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center space-x-2">
            <Code2 className="h-6 w-6 text-blue-400" />
            <span className="text-xl font-semibold code-font">Trade_Peeps</span>
          </div>

          <div className="hidden md:flex items-center space-x-8">
            <a
              href="#"
              className="text-muted-foreground hover:text-foreground transition-colors"
            >
              Home
            </a>
            <a
              href="about"
              className="text-muted-foreground hover:text-foreground transition-colors"
            >
              About Us
            </a>
            <a
              href="api/hfts"
              className="text-muted-foreground hover:text-foreground transition-colors"
            >
              HFTs
            </a>
            <a
              href="api/bulk-deals"
              className="text-muted-foreground hover:text-foreground transition-colors"
            >
              Bulk_Deals
            </a>
            <a
              href="blog"
              className="text-muted-foreground hover:text-foreground transition-colors"
            >
              Blog
            </a>
            <a
              href="contact"
              className="text-muted-foreground hover:text-foreground transition-colors"
            >
              Contact Us
            </a>
          </div>

          <div className="flex items-center space-x-4">
            <Button
              variant="ghost"
              className="text-muted-foreground hover:text-foreground"
            >
              Log In
            </Button>
            <Button className="bg-white text-black hover:bg-gray-200 transition-colors">
              Sign Up
            </Button>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
