import { Code2 } from "lucide-react";

const Footer = () => {
  return (
    <footer className="bg-gradient-to-br from-background via-background to-slate-900/20 text-white py-16 px-4 sm:px-6 lg:px-8 relative">
      {/* Large background text */}
      <div className="absolute inset-0 flex items-center justify-center overflow-hidden">
        <div className="text-[20rem] md:text-[25rem] lg:text-[30rem] font-bold text-zinc-950  select-none pointer-events-none whitespace-nowrap">
          Trade_Peeps
        </div>
      </div>

      <div className="max-w-7xl mx-auto relative z-10">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-12">
          {/* Logo and tagline */}
          <div className="md:col-span-1">
            <div className="flex items-center space-x-2 mb-4">
              <Code2 className="h-6 w-6 text-slate-900" />
              <span className="text-xl font-semibold code-font">
                Trade_Peeps
              </span>
            </div>
            <p className="text-gray-400 text-sm">
              Analyze the market in minutes
            </p>
          </div>

          {/* Pages */}
          <div>
            <h3 className="text-white font-medium mb-4">Pages</h3>
            <ul className="space-y-2">
              <li>
                <a
                  href="#"
                  className="text-gray-400 hover:text-white transition-colors text-sm"
                >
                  Home
                </a>
              </li>
              <li>
                <a
                  href="blog"
                  className="text-gray-400 hover:text-white transition-colors text-sm"
                >
                  Blog
                </a>
              </li>
            </ul>
          </div>

          {/* Socials */}
          <div>
            <h3 className="text-white font-medium mb-4">Socials</h3>
            <ul className="space-y-2">
              <li>
                <a
                  href="https://www.x.com/tradepeeps"
                  className="text-gray-400 hover:text-white transition-colors text-sm"
                >
                  X
                </a>
              </li>
              <li>
                <a
                  href="https://www.linkedin.com/company/tradepeeps"
                  className="text-gray-400 hover:text-white transition-colors text-sm"
                >
                  LinkedIn
                </a>
              </li>
              <li>
                <a
                  href="https://www.instagram.com/tradepeeps"
                  className="text-gray-400 hover:text-white transition-colors text-sm"
                >
                  Instagram
                </a>
              </li>
            </ul>
          </div>

          {/* Extensions and Legal */}
          <div>
            <h3 className="text-white font-medium mb-4">Functions</h3>
            <ul className="space-y-2 mb-6">
              <li>
                <a
                  href="api/bulk-deals"
                  className="text-gray-400 hover:text-white transition-colors text-sm"
                >
                  Bulk Deals
                </a>
              </li>
              <li>
                <a
                  href="api/hfts"
                  className="text-gray-400 hover:text-white transition-colors text-sm"
                >
                  HFTs
                </a>
              </li>
            </ul>

            <h3 className="text-white font-medium mb-4">Legal</h3>
            <ul className="space-y-2">
              <li>
                <a
                  href="https://beta.tradepeeps.com/disclaimer"
                  className="text-gray-400 hover:text-white transition-colors text-sm"
                >
                  Disclaimer
                </a>
              </li>
              <li>
                <a
                  href="https://beta.tradepeeps.com/refund-policy"
                  className="text-gray-400 hover:text-white transition-colors text-sm"
                >
                  Cancellation and refund policy
                </a>
              </li>
              <li>
                <a
                  href="https://beta.tradepeeps.com/terms-and-conditions"
                  className="text-gray-400 hover:text-white transition-colors text-sm"
                >
                  Terms and conditions
                </a>
              </li>
              <li>
                <a
                  href="https://beta.tradepeeps.com/privacy-policy"
                  className="text-gray-400 hover:text-white transition-colors text-sm"
                >
                  Privacy policy
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
