import GlobalCard from "@/app/(Containers)/GlobalCard";

type Props ={
    children: React.ReactNode;
}

export default function MainPage({children}: Props) {
    return (
        <div className="space-y-8">
            {children}
            <div className="w-96">
                <GlobalCard/>
            </div>
        </div>
    )
}