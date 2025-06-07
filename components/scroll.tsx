"use client";
import React from "react";
import { ContainerScroll } from "@/components/ui/container-scroll-animation";

export function Scroll() {
  return (
    <div className="flex flex-col overflow-hidden">
      <ContainerScroll
        titleComponent={
          <>
            <h1 className="text-4xl font-semibold text-white dark:text-white">
              Unleash the power of <br />
              <span className="text-4xl md:text-[6rem] font-bold mt-1 leading-none">
                Stocks using Trade_Peeps
              </span>
            </h1>
          </>
        }
      >
        <img
          src={`/image-1.png`}
          alt="hero"
          height={720}
          width={1400}
          className="mx-auto rounded-2xl object-cover h-full object-left-top"
          draggable={false}
        />
      </ContainerScroll>
    </div>
  );
}
